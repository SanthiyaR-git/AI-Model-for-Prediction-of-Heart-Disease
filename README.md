# 🩺 AI Model for Prediction of Heart Disease

### Project Title: Heart Disease Prediction — End-to-End Web Application

A **full-stack web app** that lets a user input medical features and get a prediction on whether they are at risk of heart disease.  
The app also stores each prediction in a **database** for later review.

---

## 🧠 Project Overview

Heart disease is a major health concern globally. Early prediction can help in preventive care.  
This project uses **machine learning** to build a predictive model based on known medical risk features and wraps it in a **web application** for user interaction.

### 🔑 Key Components
- **Dataset:** Cleveland Heart Disease dataset from UCI / Kaggle  
- **Model:** Logistic Regression (you can extend to other algorithms)  
- **Backend:** Flask API that handles form submissions, prediction logic, and database writes  
- **Database:** SQLite (stores each user’s input + prediction result)  
- **Frontend:** HTML / CSS form for user input and output display  
- **Implementation:** All logic (model training, web routes, DB) in a single file for simplicity  

---

## 📊 Dataset Description

**Dataset Source:**  
[Kaggle — Heart Disease Cleveland UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

This dataset is derived from the **UCI Machine Learning Repository’s Cleveland Heart Disease database**.  
It contains patient data with 14 attributes (features) and a target label indicating the presence or absence of heart disease.

### 🧾 Features (Input Variables)

| Feature  | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| age       | Age in years                                                      |
| sex       | Sex (1 = male; 0 = female)                                        |
| cp        | Chest pain type (0–3)                                             |
| trestbps  | Resting blood pressure (in mm Hg)                                 |
| chol      | Serum cholesterol in mg/dl                                        |
| fbs       | Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)             |
| restecg   | Resting electrocardiographic results (0–2)                        |
| thalach   | Maximum heart rate achieved                                       |
| exang     | Exercise induced angina (1 = yes; 0 = no)                         |
| oldpeak   | ST depression induced by exercise relative to rest                |
| slope     | The slope of the peak exercise ST segment (0–2)                   |
| ca        | Number of major vessels (0–3) colored by fluoroscopy              |
| thal      | Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect) |
| target    | (0 = no heart disease, 1 = presence of heart disease)             |

---

## ⚙️ Features & Functionality

- Automatically **trains the model** on first run (if not already saved)
- Applies **standard scaling** for numerical consistency
- Web page accepts all **required medical inputs**
- **Instant prediction** displayed on screen (“High Risk” or “Likely No Disease”)
- All data (inputs + prediction) stored in a **local SQLite database (`heart.db`)**
- Easy to extend — add more models, routes, or dashboards

---

## 🚀 Setup & Usage Instructions

1. **Clone / Download** this repository  
2. Download the dataset `heart.csv` from the Kaggle link above, and place it in the project root  
3. Ensure you have **Python ≥ 3.7** installed  
4. Install the required Python packages:

   ```bash
   pip install flask pandas scikit-learn joblib

**Run the application:**

python app.py

**Open your browser and visit:**

http://127.0.0.1:5000/

Fill in the form and click Predict
View the prediction on screen — your data and result are stored in heart.db

**Suggested Repository Structure**

heart-disease-predictor/
│
├── app.py                # Main Python file (model + web + DB logic)
├── heart.csv             # Dataset file (downloaded from Kaggle)
├── heart_model.pkl       # Saved trained model (auto-generated)
├── scaler.pkl            # Saved scaler object (auto-generated)
├── heart.db              # SQLite database (auto-created)
├── README.md             # Project description (this file)
└── requirements.txt      # List of dependencies (optional)


Potential Extensions & Improvements

Use advanced ML models (Random Forest, XGBoost, Neural Networks)

Add feature importance or explainable AI (SHAP, LIME)

Build an admin dashboard to view saved predictions

Implement user authentication to track user history

Deploy the app on Heroku, AWS, or Render

Use PostgreSQL / MySQL for scalable data storage

Improve UI/UX with better input validation and responsiveness

---

✅ **Tips before committing:**
- Save this as `README.md`
- Add a project banner or screenshot (`![App Screenshot](screenshot.png)`) at the top for visual appeal.
- Add a “Demo” section if you host it later (e.g., Heroku/Render).

Would you like me to include a **section for screenshots and GitHub badges** (like build status, stars, Python version, etc.) to make it look even more professional?

**Dataset Citation**

Dataset: Heart Disease Cleveland UCI — Kaggle

Originally from the UCI Machine Learning Repository.


Built with:

Python, Flask, Pandas, Scikit-learn, SQLite, and HTML/CSS

