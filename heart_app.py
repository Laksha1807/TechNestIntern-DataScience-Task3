import streamlit as st
import pandas as pd
import joblib

# Load the trained model pipeline
model = joblib.load("heart_disease_model.pkl")

# UI elements
st.title("Heart Disease Prediction App")

# Collect user input
age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", ["M", "F"])
chest_pain = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure", min_value=0, value=120)
cholesterol = st.number_input("Cholesterol", min_value=0, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.number_input("Max Heart Rate", min_value=0, value=150)
exercise_angina = st.selectbox("Exercise-induced Angina", ["Y", "N"])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Prepare input data
input_data = pd.DataFrame([{
    "Age": age,
    "Sex": sex,
    "ChestPainType": chest_pain,
    "RestingBP": resting_bp,
    "Cholesterol": cholesterol,
    "FastingBS": fasting_bs,
    "RestingECG": resting_ecg,
    "MaxHR": max_hr,
    "ExerciseAngina": exercise_angina,
    "Oldpeak": oldpeak,
    "ST_Slope": st_slope
}])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of Heart Disease")
    else:
        st.success("✅ Low risk of Heart Disease")
