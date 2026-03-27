import streamlit as st
import duckdb
import pandas as pd
import pydeck as pdk

st.set_page_config(layout="wide")

st.title("🌪️ Tornado Risk Intelligence Dashboard")

st.markdown("""
Analyze tornado patterns across the U.S.  
Explore **frequency, severity, and risk modeling** by time and location.
""")

# =============================
# LOAD DATA (CACHED)
# =============================
@st.cache_data
def load_data():
    conn = duckdb.connect("tornado_database.duckdb", read_only=True)
    return conn.execute("SELECT * FROM ef1_plus_tornadoes").df()

df = load_data()

# =============================
# CLEAN DATA
# =============================
df["MAGNITUDE"] = pd.to_numeric(df["MAGNITUDE"], errors="coerce")
df["BEGIN_TIME"] = df["BEGIN_TIME"].astype(str).str.zfill(4)
df["HOUR"] = pd.to_datetime(df["BEGIN_TIME"], format="%H%M", errors="coerce").dt.hour

# =============================
# FILTERS
# =============================
years = st.slider("Select Year Range", 1950, 2025, (2000, 2020))

states = st.multiselect(
    "Select States",
    options=sorted(df["STATE"].dropna().unique()),
    default=sorted(df["STATE"].dropna().unique())[:5]
)

hours = st.slider("Select Hour of Day", 0, 23, (0, 23))

filtered_df = df[
    (df["YEAR"].between(years[0], years[1])) &
    (df["STATE"].isin(states)) &
    (df["HOUR"].between(hours[0], hours[1]))
].copy()

# =============================
# CLASSIFICATION
# =============================
filtered_df["IMPACT_SCORE"] = filtered_df["INJURIES_DIRECT"].fillna(0)

if filtered_df["IMPACT_SCORE"].sum() == 0:
    filtered_df["AREA_TYPE"] = "Low Impact"
else:
    threshold = filtered_df["IMPACT_SCORE"].quantile(0.75)
    filtered_df["AREA_TYPE"] = filtered_df["IMPACT_SCORE"].apply(
        lambda x: "High Impact" if x > threshold else "Low Impact"
    )

# =============================
# KEY STATS
# =============================
st.subheader("📊 Key Stats")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tornadoes", f"{len(filtered_df):,}")
col2.metric("Avg Magnitude", round(filtered_df["MAGNITUDE"].mean(), 2))
col3.metric("Total Injuries", f"{int(filtered_df['INJURIES_DIRECT'].sum()):,}")

night_tornadoes = filtered_df[
    (filtered_df["HOUR"] >= 18) | (filtered_df["HOUR"] <= 6)
]
col4.metric("🌙 Night Tornadoes", f"{len(night_tornadoes):,}")

# =============================
# EXECUTIVE SUMMARY
# =============================
st.subheader("🧾 Executive Summary")

if len(filtered_df) > 0:
    st.success(f"""
- 🌪️ Most Active State: {filtered_df['STATE'].value_counts().idxmax()}  
- ⏰ Peak Tornado Hour: {int(filtered_df['HOUR'].mode()[0])}:00  
- 📊 Total Events Analyzed: {len(filtered_df):,}
""")

# =============================
# TREND
# =============================
st.subheader("📈 Tornado Trend Over Time")

trend_df = filtered_df.groupby("YEAR").size().reset_index(name="Count")
trend_df["Smoothed"] = trend_df["Count"].rolling(3).mean()
st.line_chart(trend_df.set_index("YEAR"))

# =============================
# DAY VS NIGHT
# =============================
st.subheader("🌙 Day vs Night Analysis")

day_df = filtered_df[(filtered_df["HOUR"] > 6) & (filtered_df["HOUR"] < 18)]
night_df = filtered_df[(filtered_df["HOUR"] >= 18) | (filtered_df["HOUR"] <= 6)]

st.write("### 🌪️ Tornado Count")
st.bar_chart(pd.DataFrame({
    "Day": [len(day_df)],
    "Night": [len(night_df)]
}).T)

st.write("### 🚑 Total Injuries")
st.bar_chart(pd.DataFrame({
    "Day": [day_df["INJURIES_DIRECT"].sum()],
    "Night": [night_df["INJURIES_DIRECT"].sum()]
}).T)

# =============================
# IMPACT
# =============================
st.subheader("🔥 High Impact vs Low Impact Tornadoes")

area_df = filtered_df.groupby("AREA_TYPE").agg(
    tornado_count=("AREA_TYPE", "count"),
    total_injuries=("INJURIES_DIRECT", "sum")
)

area_df["injuries_per_tornado"] = (
    area_df["total_injuries"] / area_df["tornado_count"]
)

st.bar_chart(area_df["injuries_per_tornado"])

# =============================
# STATE RISK
# =============================
st.subheader("🔥 Top 10 Most Dangerous States")

state_df = filtered_df.groupby("STATE").agg(
    tornado_count=("STATE", "count"),
    total_injuries=("INJURIES_DIRECT", "sum")
)

state_df = state_df[state_df["tornado_count"] >= 20]

state_df["injuries_per_tornado"] = (
    state_df["total_injuries"] / state_df["tornado_count"]
)

state_weight = st.slider("⚖️ State Risk Weight", 0.0, 1.0, 0.5)

state_df["inj_norm"] = state_df["injuries_per_tornado"] / state_df["injuries_per_tornado"].max()
state_df["count_norm"] = state_df["tornado_count"] / state_df["tornado_count"].max()

state_df["risk_score"] = (
    state_df["inj_norm"] * state_weight +
    state_df["count_norm"] * (1 - state_weight)
)

top_states = state_df.sort_values("risk_score", ascending=False).head(10)

st.bar_chart(top_states["risk_score"])
st.dataframe(top_states)

# =============================
# MAIN RISK MODEL
# =============================
st.subheader("🧠 Tornado Risk Score (Time + Place)")

combo = filtered_df.groupby(["STATE", "HOUR"]).agg(
    tornado_count=("STATE", "count"),
    total_injuries=("INJURIES_DIRECT", "sum")
)

combo = combo[combo["tornado_count"] >= 10]

combo["injuries_per_tornado"] = (
    combo["total_injuries"] / combo["tornado_count"]
)

weight = st.slider("⚖️ Severity vs Frequency", 0.0, 1.0, 0.5)

combo["inj_norm"] = combo["injuries_per_tornado"] / combo["injuries_per_tornado"].max()
combo["cnt_norm"] = combo["tornado_count"] / combo["tornado_count"].max()

combo["risk_score"] = (
    combo["inj_norm"] * weight +
    combo["cnt_norm"] * (1 - weight)
)

combo["confidence"] = (
    combo["tornado_count"] / combo["tornado_count"].max()
)

top5 = combo.sort_values("risk_score", ascending=False).head(5).reset_index()

# 🔥 highlight
if not top5.empty:
    worst = top5.iloc[0]
    st.warning(f"""
⚠️ Highest Risk Window: {worst['STATE']} at {int(worst['HOUR'])}:00  
Risk Score: {round(worst['risk_score'], 2)}
""")

st.dataframe(top5)

# 🔍 explanation
if not top5.empty:
    best = top5.iloc[0]

    st.subheader("🔍 Why is this the highest risk?")

    st.write(f"""
**Location:** {best['STATE']}  
**Hour:** {int(best['HOUR'])}:00  

- 🌪️ Tornado Count: {int(best['tornado_count'])}
- 🚑 Injuries per Tornado: {round(best['injuries_per_tornado'], 2)}
- ⚖️ Risk Score: {round(best['risk_score'], 2)}
- 📊 Confidence: {round(best['confidence'], 2)}
""")

# download
st.download_button(
    "📥 Download Top Risk Insights",
    top5.to_csv(index=False),
    "tornado_risk.csv"
)