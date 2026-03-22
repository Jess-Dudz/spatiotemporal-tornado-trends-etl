# The Great Migration & The Nocturnal Creep: A Spatiotemporal & Predictive Analysis of U.S. Tornado Trends

**Author:** Jessica Dudzinski  
**Role:** Data Scientist / MSDS Candidate

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Fast_Analytical_SQL-yellow.svg)](https://duckdb.org/)
[![scikit-learn](https://img.shields.io/badge/Machine_Learning-scikit--learn-orange.svg)](https://scikit-learn.org/)

## 🌪️ Executive Summary
[cite_start]This project investigates two simultaneous, high-impact shifts in U.S. tornado activity over the last 75 years: the geographic migration away from the Central Plains toward the Southeast/Midwest, and the temporal shift toward a higher frequency of nocturnal touchdowns[cite: 4]. 

[cite_start]By engineering a unified dataset from the NOAA Storm Events Database and integrating it with the CDC's Social Vulnerability Index (SVI)[cite: 5, 22, 23], this project moves beyond traditional historical weather tracking. [cite_start]It utilizes machine learning to forecast localized probability scores for nocturnal tornado occurrences, providing actionable risk-modeling for adjusting long-term disaster preparedness and building codes in emerging high-risk zones[cite: 34, 35].

## 📊 Problem Statement
[cite_start]Traditional "Tornado Alley" (Oklahoma, Kansas, Texas) has historically been synonymous with late-afternoon, spring-season storms[cite: 7]. [cite_start]However, emerging data indicates the formation of a "New Alley" in the Southeast where tornadoes are occurring more frequently, often during winter months, and crucially, at night[cite: 8]. [cite_start]Because nighttime tornadoes are statistically more lethal, quantifying and predicting this "Nocturnal Creep" is a critical public safety objective[cite: 9].

## 🔬 Core Hypotheses
1. [cite_start]**Spatial Shift:** The geographic centroid (center of gravity) of EF1+ tornadoes has shifted significantly Eastward and Northward since 1950[cite: 13].
2. [cite_start]**Temporal Shift:** The percentage of tornadoes touching down during "nocturnal hours" (8:00 PM - 6:00 AM) has increased, particularly in the Southeast and Midwest[cite: 14, 15].
3. [cite_start]**Socioeconomic Impact:** The intersection of these spatial and temporal shifts occurs in regions with higher social vulnerability, leading to a compounded risk of casualties[cite: 16].

## 🛠️ Technical Stack & Methodology

### 1. Data Engineering (The "Master Stitch")
* [cite_start]**Tool:** SQL (DuckDB) [cite: 18]
* [cite_start]**Process:** Aggregated 75+ individual annual CSV files from the NOAA NCEI database into a unified, high-performance analytical table[cite: 22, 23]. 
* [cite_start]**Quality Control:** Applied filters to restrict the analysis strictly to EF1+ events, effectively eliminating modern "reporting bias" introduced by the smartphone era[cite: 24].

### 2. Spatiotemporal Analysis
* **Tool:** Python (Pandas, GeoPandas, SciPy)
* [cite_start]**Process:** Converted UTC timestamps to local solar time based on exact touchdown coordinates to accurately classify "Nocturnal" vs. "Diurnal" events[cite: 28]. [cite_start]Calculated annual mean latitudes/longitudes to track the migration path [cite: 27][cite_start], and validated trends using the Mann-Kendall Trend Test[cite: 29].

### 3. Predictive Forecasting (Machine Learning)
* **Tool:** Python (scikit-learn)
* **Process:** Developed a Random Forest classification model to forecast the localized probability of nocturnal EF1+ events. Engineered features include localized temporal indicators, rolling decadal geospatial centroids, and SVI weights to penalize algorithmic misses in highly vulnerable counties. 

## 📂 Repository Structure
```text
├── data/
│   ├── raw/               # Raw NOAA and CDC CSV files
│   └── processed/         # Cleaned DuckDB output tables
├── notebooks/
│   ├── 01_duckdb_etl.ipynb           # The Master Stitch data pipeline
│   ├── 02_spatiotemporal_eda.ipynb   # Visualizing the migration & nocturnal creep
│   └── 03_ml_forecasting.ipynb       # Random Forest predictive modeling
├── src/
│   ├── sql_queries/       # Modular SQL scripts
│   └── utils.py           # Python helper functions (e.g., UTC to Solar Time)
├── visual_outputs/        # Decadal heatmaps and polar clock plots
├── requirements.txt       # Project dependencies
└── README.md
