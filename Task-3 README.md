# 🫀 Heart Disease Prediction Web App

## 📌 Project Overview

This Streamlit-based web application predicts the likelihood of a person having heart disease based on key medical parameters. Developed as **Task 3** of my **Data Science Internship at TechNest**, this project combines machine learning with an interactive UI for real-time predictions.

---

## 🚀 Features

- 🧠 Trained Logistic Regression Model using Scikit-Learn  
- 🖥 Streamlit Web App for real-time predictions  
- 📊 Input Features: age, sex, chest pain type, blood pressure, cholesterol, and more  
- 🔍 Scalable and deployable using GitHub + Streamlit Cloud  
- 💾 Model saved using `joblib` for fast I/O  

---

## ⚙️ How It Works

### 1. Dataset
- Source: [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets)
- Features used:  
  - `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`,  
  - `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`
- Target: `target` (0 = No Heart Disease, 1 = Heart Disease)

### 2. Preprocessing & Model
- Missing values handling
- Feature scaling using `StandardScaler`
- Model trained using Logistic Regression
- Model serialized with `joblib`

### 3. Web Application
- Takes user input through a simple form
- Passes input to the trained model
- Displays the prediction: **"At Risk"** or **"Healthy"**

###🧠 Behind the scenes:

The model outputs 1 for "At risk of heart disease"

And 0 for "Not at risk"

This output is then displayed in plain, human-readable form on the web app UI as:

✅ "The person is not likely to have heart disease."
❗ "The person is likely to have heart disease."

---

## 🛠 Tech Stack

| Layer         | Technology         |
| -------------|--------------------|
| Frontend     | Streamlit          |
| Backend      | Python, Scikit-learn |
| Deployment   | Streamlit Cloud, GitHub |
| Model Format | joblib `.pkl`      |

---

## 📁 Project Structure



Clean and responsive UI

Deployable on Streamlit Cloud

Fully integrated with GitHub

## 🧪 How to Run Locally

```bash
git clone https://github.com/Laksha1807/TechNestIntern-Data-Science.git
cd TechNestIntern-Data-Science/heart_disease_app
pip install -r requirements.txt
streamlit run heart_app.py

