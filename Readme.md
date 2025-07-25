# 🧠 Diabetes Prediction App using Machine Learning & Streamlit

This is a **machine learning–powered web app** that predicts whether a person is **diabetic or not**, based on basic health parameters taken from a medical report.

It’s designed to be **simple, clean, and trustworthy** — even for users with no technical background.

---

## 📊 Dataset Used

- **Name**: Pima Indians Diabetes Dataset  
- **Source**: [Kaggle Dataset Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)  
- **Total Rows**: 768  
- **Target Variable**: `Outcome` (1 = Diabetic, 0 = Not Diabetic)

**Features Used**:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

## ⚙️ How the App Works

1. User opens the app
2. Inputs values from their medical report
3. Clicks **“Predict”**
4. The app shows:
   - ✅ “Not Diabetic”  
   - 🛑 “Diabetic”  

---

## 💻 Tech Stack

| Component        | Tool / Library        |
|------------------|------------------------|
| Programming Lang.| Python                 |
| ML Library       | scikit-learn           |
| UI Framework     | Streamlit              |
| Data Handling    | pandas, numpy          |
| Model Saving     | pickle                 |
| Deployment       | Render.com / HuggingFace |
