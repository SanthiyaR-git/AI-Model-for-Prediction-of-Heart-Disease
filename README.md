# AI-Model-for-Prediction-of-Heart-Disease
Project Title: Heart Disease Prediction — End-to-End Web Application
A full-stack web app that lets a user input medical features and get a prediction whether they are at risk of heart disease. The app also stores each prediction in a database for later review.

**🧠 Project Overview**
Heart disease is a major health concern globally. Early prediction can help in preventive care. This project uses machine learning to build a predictive model based on known medical risk features, and wraps it in a web application so end users can interact with it.

**Key components:**
Dataset: Cleveland Heart Disease dataset from UCI / Kaggle
Model: Logistic Regression (or you can extend to other algorithms)
Backend: Flask API that handles form submissions, prediction logic, and database writes
Database: SQLite for simplicity, storing each user’s input + prediction result
Frontend: HTML / CSS form for users to input their data and view result
Single file implementation: All logic (model training, web routes, DB) in one file (for simplicity)4

Dataset Description

Dataset source:
Heart Disease Cleveland UCI on Kaggle
Link:https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci?utm_source=chatgpt.com
This dataset is derived from the UCI Machine Learning Repository’s Cleveland Heart Disease database. It contains data collected from patients, with 14 commonly used attributes (features) plus a target label indicating presence or absence of heart disease.

**Features (input variables):**
Typical columns include (but may vary slightly depending on version):
| Feature  | Description                                                       |
| -------- | ----------------------------------------------------------------- |
| age      | Age in years                                                      |
| sex      | Sex (1 = male; 0 = female)                                        |
| cp       | Chest pain type (0–3)                                             |
| trestbps | Resting blood pressure (in mm Hg)                                 |
| chol     | Serum cholesterol in mg/dl                                        |
| fbs      | Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)             |
| restecg  | Resting electrocardiographic results (0–2)                        |
| thalach  | Maximum heart rate achieved                                       |
| exang    | Exercise induced angina (1 = yes; 0 = no)                         |
| oldpeak  | ST depression induced by exercise relative to rest                |
| slope    | The slope of the peak exercise ST segment (0–2)                   |
| ca       | Number of major vessels (0–3) colored by fluoroscopy              |
| thal     | Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect) |
| target   | (0 = no heart disease, 1 = presence of heart disease)             |

**Features & Functionality**
When first run, the app trains the model (if not already saved).
A scaler is also fitted to standardize feature values.
The web page accepts user inputs for all required medical features.
Submitting the form triggers a prediction (0 or 1) and shows a human-friendly message (“High Risk” or “Likely No Disease”).
Each user input + prediction is stored in a local SQLite database (heart.db) for audit or review.
Simple and extendable — you can later add extra routes (e.g. view past predictions, admin dashboard, other ML models).

**Setup & Usage Instructions**
Clone / download this repo to your machine.
Download the dataset heart.csv from the Kaggle link above, and place it in the project root.
Ensure you have Python installed (version ≧ 3.7).
**Install required Python packages:**
pip install flask pandas scikit-learn joblib
**Run the Python script (e.g., app.py):**
python app.py
Open your browser and go to http://127.0.0.1:5000/
Fill in the form fields and click Predict
The result is displayed on screen, and stored in heart.db (SQLite).

**Suggested Repository Structure**
heart-disease-predictor/
│
├── app.py                # Main Python file (model + web + DB logic)
├── heart.csv             # Raw dataset file
├── heart_model.pkl       # Saved trained model (auto-generated)
├── scaler.pkl            # Saved scaler object (auto-generated)
├── heart.db               # SQLite database (auto-created)
├── README.md             # This project description (you)
└── requirements.txt      # List of Python dependencies (optional)

**requirements.txt :**
flask
pandas
scikit-learn
joblib

**Potential Extensions & Improvements**
Use more advanced models like Random Forest, XGBoost, or Neural Networks
Add feature importance or explainable AI (SHAP, LIME)
Create a dashboard route to view all saved predictions
Add user authentication to track each user’s history
Host the app on a cloud platform (Heroku, AWS, etc.)
Use a more scalable database (PostgreSQL, MySQL)
Add input validation, better UI/UX, mobile responsiveness, etc.

