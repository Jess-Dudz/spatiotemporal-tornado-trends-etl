# 🌪️ Tornado Risk Intelligence Dashboard

An interactive data science application that analyzes tornado risk across the United States using a dynamic scoring model.

🔗 **Live App:**
https://spatiotemporal-tornado-trends-etl-33lzqces6fp8zwndje4ch6.streamlit.app/

---

## 📊 Overview

This project transforms historical tornado data into an interactive **risk intelligence system**.

It allows users to:

* Identify high-risk locations and time windows
* Compare frequency vs severity of tornado events
* Explore how risk changes across geography and time
* Analyze confidence based on sample size

---

## 🧠 Key Insights

### 🌍 The Great Migration

Tornado activity has shifted eastward from the traditional Central Plains toward the Southeast ("Dixie Alley"), increasing exposure in more densely populated regions.

### 🌙 The Nocturnal Creep

Tornadoes are increasingly occurring at night, when detection and response are more difficult, increasing overall risk.

---

## 🧠 Risk Model

The dashboard includes a dynamic risk model combining:

* **Frequency** → number of tornadoes
* **Severity** → injuries per tornado

Risk Score = (Severity × weight) + (Frequency × (1 - weight))

Users can adjust the weighting to explore different definitions of risk.

---

## 🚀 Features

* Interactive filtering (state, year, time of day)
* Trend analysis over time
* Day vs night comparisons
* High-impact tornado classification
* State-level composite risk rankings
* Time + place risk modeling
* Confidence scoring (sample size awareness)
* Downloadable insights
* Optional geographic heatmap

---

## ⚙️ Tech Stack

* Python
* Streamlit
* DuckDB
* Pandas
* PyDeck

---

## 🔬 Machine Learning Analysis (Research Layer)

This project also includes a deeper modeling pipeline exploring nocturnal tornado prediction.

### Problem

Tornado events are highly imbalanced:

* ~80% occur during daytime
* Nighttime events are rarer but more dangerous

### Solution

A SMOTE-enhanced Random Forest model was used to improve detection of nocturnal events.

### Results

| Metric           | Baseline | SMOTE Model |
| ---------------- | -------- | ----------- |
| Nocturnal Recall | 24%      | 51%         |
| Accuracy         | 84%      | 76%         |
| F1 Score         | 0.35     | 0.48        |

### Key Finding

Latitude emerged as the strongest predictor of nocturnal tornado risk, reinforcing the increased vulnerability of the Southeast.

---

## 🏗️ Data Engineering

* DuckDB used for high-performance querying
* 43,000+ EF1+ tornado records analyzed
* Local solar time engineered from longitude offsets
* Efficient ETL pipeline for large historical datasets

---

## 📁 Project Structure

app.py
tornado_database.duckdb
requirements.txt
README.md
notebooks/
visual_outputs/

---

## 🚀 How to Run Locally

pip install -r requirements.txt
streamlit run app.py

---

## 💡 Why This Project Matters

This project demonstrates:

* End-to-end data pipeline development
* Spatiotemporal feature engineering
* Risk modeling and normalization
* Handling imbalanced datasets
* Model interpretability
* Deployment of interactive analytics tools

---

## 👤 Author

Jessica Dudzinski

