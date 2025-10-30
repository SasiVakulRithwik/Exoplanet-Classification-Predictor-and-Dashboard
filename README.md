# Exoplanet Classification Dashboard 🌌

A comprehensive machine learning system that classifies celestial objects as exoplanets, candidates, or false positives using NASA's Kepler mission data.

![Exoplanet](https://img.shields.io/badge/Exoplanet-Classification-blue)
![NASA](https://img.shields.io/badge/NASA-Kepler%20Mission-red)
![Python](https://img.shields.io/badge/Python-Data%20Science-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-77.38%25-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Framework-green)
![Astronomy](https://img.shields.io/badge/Astronomy-Data%20Science-purple)

## 📊 Project Overview

The *Exoplanet Classification Dashboard* is an advanced machine learning system designed to classify celestial objects detected by NASA's Kepler mission into three categories: confirmed exoplanets, candidate exoplanets, and false positives. This project demonstrates the practical application of data science methodologies to solve complex astronomical classification problems.

By analyzing astronomical data from NASA's Exoplanet Archive, our model provides valuable insights for:

- *Automated Classification* - Rapid identification of potential exoplanets from transit signals
- *Research Efficiency* - Reducing manual verification time for astronomers
- *Data Prioritization* - Helping telescopes allocate observation time to promising candidates
- *Educational Tool* - Making exoplanet discovery accessible to students and researchers

## Website View

Prediction Page
![Prediction](/screenshots/prediction.png)

Analytics Page
![Analytics](/screenshots/analytics.png)

Dataset Page
![Dataset](/screenshots/dataset.png)

Documentation Page
![Details](/screenshots/details.png)

## 🎯 Key Features

### 🤖 Machine Learning Model

- *Algorithm*: Random Forest Classifier
- *Accuracy*: 77.38%
- *Cross-validation Score*: 76.77%
- *Features*: 16 astronomical parameters
- *Precision (Macro)*: 0.83
- *Recall (Macro)*: 0.70
- *F1-Score (Macro)*: 0.75

### 📈 Interactive Dashboard

- *Real-time Predictions*: Instant classification of celestial objects
- *Comprehensive Analytics*: Model performance metrics and visualizations
- *Dataset Exploration*: Full dataset information and feature descriptions
- *Technical Documentation*: Complete project documentation and API details

### 🔍 Data Insights

- *Total Records Analyzed*: 19,761 astronomical observations
- *Training Samples*: 15,808
- *Testing Samples*: 3,953
- *Class Distribution*: 
  - False Positives: 6,311 (31.9%)
  - Candidates: 7,413 (37.5%)
  - Confirmed Planets: 6,015 (30.4%)
  - Class 3: 22 (0.1%)

## 🏗 System Architecture

### Data Pipeline
```python
Raw Kepler Data → Data Preprocessing → Feature Engineering → Model Training → Prediction → Web Dashboard
```

### Technology Stack

- *Backend*: FastAPI, Scikit-learn, Pandas, Joblib
- *Frontend*: HTML5, CSS3, JavaScript, Chart.js
- *Machine Learning*: Random Forest, Feature Scaling, Model Persistence
- *Data Processing*: Pandas, NumPy, Data Validation

## 🔬 Machine Learning Methodology

### Dataset Selection

We selected NASA's Exoplanet Archive dataset for its:

- *Scientific Rigor*: Data from NASA's Kepler mission with peer-reviewed confirmations
- *Comprehensive Features*: 16 carefully selected astronomical parameters
- *Real Discovery Data*: Authentic exoplanet detection pipeline data
- *Research Standard*: Industry-standard astronomical measurements and classifications

### Feature Engineering

Our feature set includes 16 critical astronomical parameters:

*Top Predictive Features:*

1. *Planet Radius* (0.1459) - Size of the potential planet in Earth radii
2. *Light Curve Time 0* (0.1117) - Reference time for transit analysis
3. *Orbital Period* (0.0928) - Duration of planetary orbit in days
4. *PC3* (0.0845) - Third principal component from light curve analysis
5. *PC1* (0.0722) - First principal component from dimensionality reduction

### Feature Categories

- *Principal Components*: PC1, PC2, PC3 (dimensionality reduced features)
- *Celestial Coordinates*: Right Ascension (ra), Declination (dec)
- *Stellar Properties*: Temperature, Surface Gravity, Radius, Mass
- *Planetary Characteristics*: Radius, Orbital Period
- *Photometric Data*: J, H, K, Kepler Magnitudes
- *Light Curve Features*: Time series analysis parameters

### Algorithm Selection: Why Random Forest?

After comprehensive evaluation, we selected Random Forest for:

| Algorithm              | Accuracy  | Pros                                                          | Cons                             |
| ---------------------- | --------- | ------------------------------------------------------------- | -------------------------------- |
| *Random Forest*      | *77.38%* | Handles non-linearity, robust to outliers, feature importance | Computationally intensive        |
| Logistic Regression    | 68.2%     | Interpretable, fast training                                  | Poor with complex relationships  |
| Support Vector Machine | 72.1%     | Effective in high dimensions                                  | Poor scalability                 |
| Gradient Boosting      | 75.9%     | High predictive power                                         | Overfitting risk                 |

*Key Advantages:*

- *Feature Importance*: Clear insights into astronomical factors driving classification
- *Robustness*: Effective handling of astronomical measurement uncertainties
- *Non-linearity*: Captures complex relationships in astronomical data
- *Ensemble Method*: Reduces overfitting through multiple decision trees

## 📊 Model Performance

### Comprehensive Metrics

| Metric                  | Score     | Description                           |
| ----------------------- | --------- | ------------------------------------- |
| *Accuracy*            | *77.38%* | Overall prediction accuracy           |
| *Cross-validation*    | 76.77%    | Consistent performance across splits  |
| *Precision (Macro)*   | 0.83      | Correct positive predictions          |
| *Recall (Macro)*      | 0.70      | True positive rate                    |
| *F1-Score (Macro)*    | 0.75      | Harmonic mean of precision and recall |

### Confusion Matrix Analysis

- *False Positives*: 1,001 correctly classified, 223 misclassified as Candidates, 39 as Confirmed Planets
- *Candidates*: 1,161 correctly classified, 169 misclassified as False Positives, 153 as Confirmed Planets
- *Confirmed Planets*: 885 correctly classified, 84 misclassified as False Positives, 234 as Candidates

## 🎯 Scientific Impact

### Research Applications

- *Automated Discovery*: Accelerating initial classification of transit signals
- *Resource Optimization*: Helping telescopes prioritize follow-up observations
- *Educational Tool*: Making exoplanet research accessible to students
- *Method Validation*: Comparing machine learning approaches with traditional methods

### Key Astronomical Findings

- *Planet Radius Critical*: Most important feature for classification (14.59% importance)
- *Light Curve Analysis*: Time-series features significantly impact classification accuracy
- *Stellar Properties*: Star temperature and characteristics play moderate roles
- *Multi-feature Dependency*: Complex interactions between orbital and stellar parameters

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Dependencies listed in requirements.txt

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `uvicorn main:app --reload`
4. Access dashboard at: `http://localhost:8000`

### Usage

1. *Make Predictions*: Use the prediction page to input astronomical parameters
2. *Explore Analytics*: Navigate to analytics for model performance insights
3. *Study Dataset*: Use dataset info to understand feature descriptions
4. *Read Documentation*: Comprehensive technical details in documentation section

### API Endpoints

- `GET /api/summary` - Returns dataset statistics and summary information
- `POST /api/predict` - Makes exoplanet classification predictions

## 🌌 Target Classification

### Classification Categories

#### ❌ False Positive (Class 0)
Signals caused by instrumental errors, stellar activity, or binary star systems that mimic planetary transits
- *Instrumental artifacts*
- *Stellar variability*
- *Eclipsing binaries*
- *Systematic errors*

#### 🔍 Candidate (Class 1)
Potential exoplanets requiring further verification through additional observations and analysis
- *Promising transit signals*
- *Requires confirmation*
- *Follow-up observations needed*
- *Statistical validation required*

#### ✅ Confirmed Planet (Class 2)
Verified exoplanets with multiple detection confirmations through different methods
- *Multiple detection methods*
- *Statistical significance*
- *Peer-reviewed confirmation*
- *Published in scientific literature*

## 🔮 Future Enhancements

### Planned Features

- *Real-time Telescope Integration*: Connect with live astronomical data streams
- *Advanced Light Curve Analysis*: Incorporate full light curve processing
- *Multi-mission Data*: Integrate data from TESS, James Webb, and future missions
- *Deep Learning Integration*: Explore neural networks for complex pattern recognition
- *Citizen Science Interface*: Public participation in exoplanet discovery

### Research Directions

- *Multi-wavelength Analysis*: Incorporate infrared and radio observations
- *Atmospheric Characterization*: Predict planetary atmosphere types
- *Habitable Zone Analysis*: Identify potentially habitable exoplanets
- *Temporal Evolution*: Study how classification confidence changes with additional observations

## 📈 Data Science Significance

### Methodological Innovations

- *Astronomical Feature Engineering*: Domain-specific feature selection for exoplanet detection
- *Ensemble Learning Application*: Practical implementation in astronomical classification
- *Interpretable AI*: Balanced predictive power with scientific interpretability
- *Scalable Architecture*: Designed for integration with astronomical data pipelines

### Scientific Contribution

- *Automation of Discovery*: Demonstrating ML's role in accelerating scientific discovery
- *Standardized Methodology*: Establishing benchmarks for exoplanet classification
- *Open Science*: Making exoplanet research tools accessible to broader community
- *Educational Value*: Bridging data science and astronomy education

---

> 🌟 *Exploring the cosmos, one prediction at a time!*

> ⭐ If you find this project helpful for astronomical research, please give it a star!