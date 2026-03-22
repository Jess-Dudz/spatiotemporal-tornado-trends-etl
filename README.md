# The Great Migration & The Nocturnal Creep: A Spatiotemporal & Predictive Analysis of U.S. Tornado Trends

**Author:** Jessica Dudzinski  
**Role:** Data Scientist / MSDS Candidate

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Fast_Analytical_SQL-yellow.svg)](https://duckdb.org/)
[![scikit-learn](https://img.shields.io/badge/Machine_Learning-scikit--learn-orange.svg)](https://scikit-learn.org/)

## 1. Executive Summary
This study investigates two simultaneous shifts in U.S. tornado activity over the last 75 years: the geographic migration from the Central Plains to the Southeast/Midwest, and the temporal shift toward a higher frequency of nocturnal touchdowns. By leveraging the NOAA Storm Events Database, this project seeks to quantify how these changes increase the vulnerability of local populations and challenge existing warning systems.

## 2. Problem Statement
Traditional "Tornado Alley" is synonymous with late-afternoon, spring-season storms. However, emerging data suggests a "New Alley" in the Southeast (Dixie Alley) where tornadoes are more frequent, often occur at night, and happen during the winter months. Because nighttime tornadoes are statistically more lethal, proving and predicting this "Nocturnal Creep" is a critical public safety objective.

## 3. Core Hypotheses
* **Hypothesis 1 (Spatial):** The geographic centroid (center of gravity) of EF1+ tornadoes has shifted significantly Eastward and Northward since 1950.
* **Hypothesis 2 (Temporal):** The percentage of tornadoes touching down during "nocturnal hours" (8:00 PM - 6:00 AM) has increased, particularly in the Southeast and Midwest.
* **Hypothesis 3 (Impact):** The intersection of the spatial shift and the nocturnal shift occurs in regions with higher social vulnerability (as measured by the CDC SVI), leading to a higher risk of casualties.

## 4. Project Roadmap & Agile Methodology
To ensure rigorous data validation and avoid scope creep, this project is developed in phased iterations:

### Phase 1: The Baseline MVP (Current)
* **Objective:** Establish the core spatiotemporal data pipeline and baseline predictive model.
* **Data Engineering:** Using DuckDB to aggregate 75+ individual CSV files from NOAA into a unified, out-of-memory analytical table, filtering for EF1+ events to eliminate historical reporting bias.
* **Spatiotemporal EDA:** Converting UTC timestamps to local solar time and tracking annual mean latitudes/longitudes.
* **Baseline Modeling:** Training a Random Forest classifier using strictly geospatial and temporal features to predict localized nocturnal tornado probabilities.

### Phase 2: Feature Enrichment (Planned)
* **Objective:** Improve the predictive recall of the baseline model by engineering advanced meteorological indices.
* **Climate Integration:** Ingesting historical Gulf of Mexico Sea Surface Temperatures (SST) and ENSO phase data to measure the impact of oceanic warming on the eastward migration.
* **Vulnerability Weighting:** Incorporating the CDC Social Vulnerability Index (SVI) directly into the model's loss function to penalize algorithmic misses in highly vulnerable counties.

## 5. Technical Stack
* **Languages:** SQL (DuckDB) for high-performance ETL; Python (Pandas, GeoPandas, SciPy) for spatial math and temporal normalization.
* **Machine Learning:** `scikit-learn` for predictive modeling.

## 📂 Repository Structure
```text
├── data/
│   ├── raw/               # Raw NOAA and CDC CSV files
│   └── processed/         # Cleaned DuckDB output tables
├── notebooks/
│   ├── 01_duckdb_etl.ipynb           # The Master Stitch & Data Ingestion
│   ├── 02_spatiotemporal_eda.ipynb   # Visualizing the migration & nocturnal creep
│   └── 03_ml_forecasting.ipynb       # Random Forest predictive modeling
├── src/
│   ├── sql_queries/       # Modular SQL scripts
│   └── utils.py           # Python helper functions (e.g., UTC to Solar Time)
├── visual_outputs/        # Decadal heatmaps and polar clock plots
├── requirements.txt       # Project dependencies
└── README.md
