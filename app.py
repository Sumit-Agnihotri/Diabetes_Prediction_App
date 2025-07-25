# app.py
import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Page config
st.set_page_config(page_title="🩺 Diabetes Checker", page_icon="💉", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Enter report values below to check if the person is diabetic or not</h4>", unsafe_allow_html=True)
st.markdown("---")

# Form for input
with st.form("diabetes_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.number_input("Pregnancies (No. of times pregnant)", min_value=0, max_value=20, step=1)
        Glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=1000, step=1)
        BloodPressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, step=1)
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=200, step=1)

    with col2:
        Insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0.0, max_value=2000.0, step=1.0)
        BMI = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, step=0.1)
        DPF = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, step=0.01)
        Age = st.number_input("Age (in years)", min_value=0, max_value=100, step=1)

    submitted = st.form_submit_button("🧪 Predict")

# Predict on submission
if submitted:
    input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                            Insulin, BMI, DPF, Age]])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("🛑 The person is **Diabetic**.")
    else:
        st.success("✅ The person is **Not Diabetic**.")