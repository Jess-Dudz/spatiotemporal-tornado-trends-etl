# 🌪️ The Great Migration & The Nocturnal Creep
**A Spatiotemporal Machine Learning Analysis of U.S. Tornado Shifts (1950–2025)**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![DuckDB](https://img.shields.io/badge/Database-DuckDB-yellow)
![Machine Learning](https://img.shields.io/badge/ML-Random_Forest-lightgrey)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 📌 Executive Summary
Over the last 75 years, the behavior of severe weather in the United States has fundamentally changed. This project ingests and analyzes historical NOAA data to investigate two dangerous spatiotemporal phenomena:
1. **The Great Migration:** A geographic shift of tornado density away from the traditional Central Plains (e.g., Oklahoma, Kansas) and into the Southeast (Dixie Alley).
2. **The Nocturnal Creep:** An increasing frequency of nighttime and early-morning touchdowns, which disproportionately impact vulnerable populations.

By engineering local solar time features and deploying a SMOTE-enhanced Random Forest Classifier, this project successfully models the geographic and seasonal parameters driving nocturnal tornado risk.

---

## 🏗️ Data Architecture & Engineering
Processing 75 years of raw, compressed `.csv` files required a high-performance ETL pipeline. 
* **Engine:** DuckDB was utilized to bypass pandas memory constraints, allowing for lightning-fast SQL aggregations across 43,236 distinct EF1+ tornado records.
* **Feature Engineering:** Raw UTC timestamps were converted to **Local Solar Time** using high-precision longitude offsets. This ensured that "Nocturnal" was accurately defined by actual daylight conditions at the specific touchdown location, rather than a flat time zone standard.

---

## 📊 Phase 1: Exploratory Spatial Data Analysis (ESDA)

### 1. The Nocturnal Creep (Temporal Shift)
A comparative analysis of the 1950-1985 baseline versus the modern 1990-2025 era reveals a clear expansion of tornado activity into the late-night and early-morning hours. 

<div align="center">
  <img src="visual_outputs/nocturnal_creep_clock_plot.jpg" alt="Polar Clock Plot showing Nocturnal Creep" width="600"/>
  <br>
  <i><b>Figure 1: The Nocturnal Creep.</b> A polar distribution of EF1+ tornadoes by Local Solar Hour. A comparative analysis reveals a clear temporal shift where modern tornado activity (red) is expanding into the late-night and early-morning hours compared to the 1950-1985 baseline (blue).</i>
</div>

### 2. The Great Migration (Geographic Shift)
A non-parametric Mann-Kendall trend test confirmed a statistically significant Eastward shift ($p < 0.001$). To visualize this, decadal geospatial heatmaps were generated using `geopandas`.

<div align="center">
  <img src="visual_outputs/rf_feature_importance.png" alt="Random Forest Feature Importance" width="700"/>
  <br>
  <i><b>Figure 3: Gini Feature Importance.</b> Extracted from the SMOTE-trained Random Forest Classifier. Latitude emerges as the dominant predictor of a nocturnal event, mathematically validating the physical threat of shorter winter days and proximity to Gulf moisture in the Southeast.</i>
</div>

---

## 🤖 Phase 2: Predictive Machine Learning

To transition from historical analysis to predictive forecasting, a **Random Forest Classifier** was built to predict the probability of a tornado occurring at night based strictly on its spatiotemporal coordinates (Latitude, Longitude, Month).

### Handling the Accuracy Trap
Initial modeling yielded an 84% accuracy, but a dangerously low recall (0.24) for the minority class (Nocturnal). Standard spatial features alone are heavily biased toward the more frequent daytime storms.

### SMOTE Resampling & Results
To optimize the model for disaster forecasting—where False Negatives are highly dangerous—**SMOTE (Synthetic Minority Over-sampling Technique)** was applied to the training data. 
* **Result:** Minority Recall doubled from 24% to **51%**, allowing the model to successfully identify more than half of all nocturnal events using only location and season.

### Inside the Black Box: Feature Importance
<div align="center">
  <img src="visual_outputs/rf_feature_importance.png" alt="Random Forest Feature Importance" width="700"/>
  <br>
  <i>Figure 3: Gini Importance extracted from the SMOTE-trained Random Forest.</i>
</div>

**Key Finding:** `BEGIN_LAT` (Latitude) emerged as the dominant predictor of a nocturnal event. This mathematically validates the physical reality of the threat: lower latitudes (the Southeast/Dixie Alley) have shorter winter days and closer proximity to the Gulf of Mexico's low-level moisture jet, creating the perfect engine for off-hour severe weather.

---

## 🚀 Conclusion
This analysis proves that the definition of "Tornado Alley" is no longer static. As activity pushes further South and East, it encounters areas with higher population densities, more mobile homes, and greater tree cover—all while striking increasingly under the cover of darkness. 

**Repository Structure:**
* `01_duckdb_etl.ipynb`: Data ingestion, SQL cleaning, and database generation.
* `02_spatiotemporal_eda.ipynb`: Feature engineering, Mann-Kendall testing, and geospatial mapping.
* `03_ml_forecasting.ipynb`: Predictive modeling, SMOTE resampling, and feature extraction.
