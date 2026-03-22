# The Great Migration & The Nocturnal Creep: A Spatiotemporal & Predictive Analysis of U.S. Tornado Trends

**Author:** Jessica Dudzinski  
**Role:** Data Scientist / MSDS Candidate

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![DuckDB](https://img.shields.io/badge/DuckDB-Fast_Analytical_SQL-yellow.svg)](https://duckdb.org/)
[![scikit-learn](https://img.shields.io/badge/Machine_Learning-scikit--learn-orange.svg)](https://scikit-learn.org/)

## 1. Executive Summary
This study investigates two simultaneous shifts in U.S. tornado activity over the last 75 years: the geographic migration from the Central Plains to the Southeast/Midwest, and the temporal shift toward a higher frequency of nocturnal touchdowns. By leveraging the NOAA Storm Events Database, this project seeks to quantify how these changes increase the vulnerability of local populations and challenge existing warning systems.

## 2. Problem Statement
Traditional "Tornado Alley" (Oklahoma, Kansas, Texas) is synonymous with late-afternoon, spring-season storms. However, emerging data suggests a "New Alley" in the Southeast (Dixie Alley) where tornadoes are more frequent, often occur at night, and happen during the winter months. Because nighttime tornadoes are statistically more lethal, proving this "Nocturnal Creep" is a critical public safety objective.

## 3. Core Hypotheses
* **Hypothesis 1 (Spatial):** The geographic centroid (center of gravity) of EF1+ tornadoes has shifted significantly Eastward and Northward since 1950.
* **Hypothesis 2 (Temporal):** The percentage of tornadoes touching down during "nocturnal hours" (8:00 PM - 6:00 AM) has increased, particularly in the Southeast and Midwest.
* **Hypothesis 3 (Impact):** The intersection of the spatial shift and the nocturnal shift occurs in regions with higher social vulnerability (as measured by the CDC SVI), leading to a higher risk of casualties.

## 4. Technical Stack & Data Engineering
* **Languages:** SQL (DuckDB) for high-performance ETL; Python for spatial math and visualization.
* **Data Sources:** 75 years of raw touchdown data from the NOAA NCEI Storm Events database, and county-level socioeconomic data from the CDC Social Vulnerability Index (SVI).
* **The "Master Stitch":** Using DuckDB to aggregate 75+ individual CSV files into a unified analytical table.
* **Filtering Bias:** Restricting analysis to EF1+ events to eliminate "reporting bias" from the modern smartphone era.

## 5. Analytical Methodology
* **Centroid Tracking:** Calculating annual mean latitude/longitude to visualize the migration path of "Tornado Alley".
* **Local Time Normalization:** Converting UTC timestamps to local solar time based on touchdown coordinates to accurately identify "Nocturnal" vs. "Diurnal" events.
* **Trend Validation:** Utilizing the Mann-Kendall Trend Test to confirm that the changes in time and space are statistically significant.
* **Visualizations:** Decadal Heatmaps comparing touchdown density from 1950-1985 vs. 1990-2025. Polar "Clock" Plots showing the distribution of touchdown hours to highlight the increase in nighttime activity.

## 6. Predictive Forecasting (Machine Learning)
* **Objective:** To develop a predictive model that forecasts the probability of nocturnal tornado occurrences.
* **The Model:** Utilizing a Random Forest classifier to map localized future risk.
* **Feature Engineering:** The model ingests normalized local solar time, rolling decadal geospatial centroids, and utilizes CDC SVI weights directly in the loss function to penalize algorithmic misses in highly vulnerable counties.

## 7. Significance & Impact
For residents in states like Oklahoma, understanding this shift is vital for adjusting long-term disaster preparedness. This project moves beyond "weather tracking" into "risk modeling," providing a data-driven argument for updated building codes and improved nighttime alert systems in the newly high-risk zones of the Southeast.

## 📂 Repository Structure
```text
├── data/
│   ├── raw/               # Raw NOAA and CDC CSV files
│   └── processed/         # Cleaned
