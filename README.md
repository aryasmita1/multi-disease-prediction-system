# Multi Disease Prediction System

## Overview

The Multi Disease Prediction System is a machine learning-based healthcare application developed using Python and Streamlit. The application enables users to predict the likelihood of multiple diseases by entering relevant medical parameters through a user-friendly web interface.

The system currently supports prediction for:

- Diabetes
- Heart Disease
- Breast Cancer
- Parkinson's Disease

Each disease prediction module uses a separately trained machine learning model that has been serialized and deployed within the application.

---

## Features

### Diabetes Prediction

Predicts whether a patient is diabetic based on:

- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

### Heart Disease Prediction

Predicts the likelihood of heart disease using:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression
- Slope of Peak Exercise ST Segment
- Number of Major Vessels
- Thalassemia Value

### Breast Cancer Prediction

Predicts whether a tumor is:

- Benign
- Malignant

The model uses diagnostic measurements such as:

- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Compactness
- Concavity
- Symmetry
- Fractal Dimension

### Parkinson's Disease Prediction

Predicts the presence of Parkinson's Disease using voice measurements including:

- Average Vocal Frequency
- Maximum Vocal Frequency
- Minimum Vocal Frequency
- Jitter Metrics
- Shimmer Metrics
- Noise-to-Harmonics Ratio
- Harmonics-to-Noise Ratio
- RPDE
- DFA
- Spread Metrics
- D2
- PPE

---

## Project Structure

```text
multi-disease-prediction-system-main/
│
├── test.py
│
├── diabetes_model.sav
├── heart_disease_model.sav
├── breast_cancer_model.sav
├── parkinson_disease_model.sav
│
├── diabetes.csv
├── heart_disease_data.csv
├── data.csv
├── parkinsons.csv
│
├── Diabetes Prediction.ipynb
├── Heart Disease Prediction.ipynb
├── Breast Cancer Prediction.ipynb
├── Parkinson's Disease prediction.ipynb
│
├── requirements.txt
├── runtime.txt
├── setup.sh
├── Procfile.txt
│
└── README.md
```

---

## Technology Stack

### Frontend

- Streamlit

### Backend

- Python

### Machine Learning

- Scikit-Learn
- Pickle

### Data Processing

- NumPy
- Pandas

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd multi-disease-prediction-system-main
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run test.py
```

Open the following URL in your browser:

```text
http://localhost:8501
```

---

## Application Workflow

1. User selects a disease prediction module.
2. User enters the required medical parameters.
3. Input values are preprocessed.
4. The corresponding trained model is loaded.
5. The model generates a prediction.
6. Results are displayed through the Streamlit interface.

---

# Machine Learning Models

## Diabetes Prediction Model

### Algorithm

Support Vector Machine (SVM)

```python
classifier = svm.SVC(kernel='linear')
```

### Dataset

- File: `diabetes.csv`
- Records: 768
- Features: 8
- Target Variable: Outcome

### Data Preprocessing

- StandardScaler
- Train-Test Split

### Performance

| Metric | Value |
|----------|----------|
| Training Accuracy | 78.66% |
| Test Accuracy | 77.27% |

### Classification Report

| Class | Precision | Recall | F1 Score |
|---------|---------|---------|---------|
| Non-Diabetic (0) | 0.78 | 0.91 | 0.84 |
| Diabetic (1) | 0.76 | 0.52 | 0.62 |

---

## Heart Disease Prediction Model

### Algorithm

Logistic Regression

```python
model = LogisticRegression()
```

### Dataset

- File: `heart_disease_data.csv`
- Records: 303
- Features: 13

### Performance

| Metric | Value |
|----------|----------|
| Training Accuracy | 83.06% |
| Test Accuracy | 90.16% |

### Classification Report

| Class | Precision | Recall | F1 Score |
|---------|---------|---------|---------|
| No Heart Disease (0) | 1.00 | 0.81 | 0.90 |
| Heart Disease (1) | 0.83 | 1.00 | 0.91 |

---

## Breast Cancer Prediction Model

### Algorithm

Support Vector Machine (Linear Kernel)

```python
model = svm.SVC(kernel='linear')
```

### Dataset

- Wisconsin Breast Cancer Dataset
- Records: 569
- Features: 30

### Performance

| Metric | Value |
|----------|----------|
| Training Accuracy | 96.92% |
| Test Accuracy | 94.74% |

### Classification Report

| Class | Precision | Recall | F1 Score |
|---------|---------|---------|---------|
| Malignant (0) | 0.93 | 0.93 | 0.93 |
| Benign (1) | 0.96 | 0.96 | 0.96 |

---

## Parkinson's Disease Prediction Model

### Algorithm

Support Vector Machine (SVM)

```python
model = svm.SVC(kernel='linear')
```

### Dataset

- File: `parkinsons.csv`
- Records: 195
- Features: 22

### Data Preprocessing

- StandardScaler
- Train-Test Split

### Performance

| Metric | Value |
|----------|----------|
| Training Accuracy | 89.74% |
| Test Accuracy | 89.74% |

### Classification Report

| Class | Precision | Recall | F1 Score |
|---------|---------|---------|---------|
| Healthy (0) | 0.80 | 0.80 | 0.80 |
| Parkinson's Disease (1) | 0.93 | 0.93 | 0.93 |

---

## Performance Summary

| Disease | Algorithm | Training Accuracy | Test Accuracy |
|----------|------------|------------------|--------------|
| Diabetes Prediction | SVM (Linear Kernel) | 78.66% | 77.27% |
| Heart Disease Prediction | Logistic Regression | 83.06% | 90.16% |
| Breast Cancer Prediction | SVM (Linear Kernel) | 96.92% | 94.74% |
| Parkinson's Disease Prediction | SVM (Linear Kernel) | 89.74% | 89.74% |

---

## Trained Model Files

| Model File | Purpose |
|------------|----------|
| diabetes_model.sav | Diabetes Prediction |
| heart_disease_model.sav | Heart Disease Prediction |
| breast_cancer_model.sav | Breast Cancer Prediction |
| parkinson_disease_model.sav | Parkinson's Disease Prediction |

---

## Datasets

| Dataset File | Purpose |
|-------------|---------|
| diabetes.csv | Diabetes Model Training |
| heart_disease_data.csv | Heart Disease Model Training |
| data.csv | Breast Cancer Model Training |
| parkinsons.csv | Parkinson's Disease Model Training |

---

## Jupyter Notebooks

The project contains separate notebooks for model development and experimentation:

- Diabetes Prediction.ipynb
- Heart Disease Prediction.ipynb
- Breast Cancer Prediction.ipynb
- Parkinson's Disease prediction.ipynb

The notebooks include:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Model Serialization using Pickle

---

## Python Libraries Used

### Core Libraries

```text
numpy
pandas
streamlit
pickle
scikit-learn
```

### Scikit-Learn Components

```text
SVC
LogisticRegression
StandardScaler
train_test_split
accuracy_score
classification_report
```

---

## Deployment Configuration

| File | Purpose |
|--------|----------|
| requirements.txt | Dependency Management |
| runtime.txt | Python Runtime Configuration |
| setup.sh | Environment Setup Script |
| Procfile.txt | Deployment Configuration |

---

## Future Enhancements

- User Authentication
- Prediction History Tracking
- Probability Score Display
- Explainable AI (XAI)
- REST API Support
- Cloud Deployment
- Additional Disease Prediction Modules
- Mobile Responsive Interface

---

## Disclaimer

This application is intended solely for educational, research, and demonstration purposes. The predictions generated by the system should not be considered medical advice, diagnosis, or treatment recommendations. Always consult qualified healthcare professionals for medical decisions.

