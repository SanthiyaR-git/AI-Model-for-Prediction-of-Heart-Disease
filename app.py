from flask import Flask, render_template_string, request, redirect
import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib
import os

app = Flask(__name__)

# =========================
# STEP 1: LOAD & TRAIN MODEL
# =========================
MODEL_PATH = "heart_model.pkl"
SCALER_PATH = "scaler.pkl"

if not os.path.exists(MODEL_PATH):
    df = pd.read_csv("heart.csv")

    # Clean dataset
    df = df.dropna()

    X = df.drop("target", axis=1)
    y = df["target"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_scaled, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
else:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

# =========================
# STEP 2: DATABASE SETUP
# =========================
def init_db():
    conn = sqlite3.connect("heart.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    sex INTEGER,
                    cp INTEGER,
                    trestbps INTEGER,
                    chol INTEGER,
                    fbs INTEGER,
                    restecg INTEGER,
                    thalach INTEGER,
                    exang INTEGER,
                    oldpeak REAL,
                    slope INTEGER,
                    ca INTEGER,
                    thal INTEGER,
                    result TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# =========================
# STEP 3: FRONTEND TEMPLATE
# =========================
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Heart Disease Prediction</title>
    <style>
        body {font-family: Arial; background: #f0f3f5; padding: 30px;}
        h1 {text-align: center; color: #333;}
        form {background: white; padding: 25px; border-radius: 10px; width: 400px; margin: auto; box-shadow: 0px 0px 10px #ccc;}
        input, select {width: 100%; padding: 8px; margin: 6px 0;}
        button {background-color: #28a745; color: white; padding: 10px; width: 100%; border: none; border-radius: 5px;}
        .result {text-align: center; margin-top: 20px; font-size: 20px;}
    </style>
</head>
<body>
    <h1>Heart Disease Predictor 💓</h1>
    <form method="POST" action="/predict">
        <input type="text" name="name" placeholder="Enter your name" required>
        <input type="number" name="age" placeholder="Age" required>
        <select name="sex" required>
            <option value="1">Male</option>
            <option value="0">Female</option>
        </select>
        <input type="number" name="cp" placeholder="Chest Pain Type (0-3)" required>
        <input type="number" name="trestbps" placeholder="Resting BP" required>
        <input type="number" name="chol" placeholder="Cholesterol" required>
        <input type="number" name="fbs" placeholder="Fasting Blood Sugar (>120mg/dl, 1=True, 0=False)" required>
        <input type="number" name="restecg" placeholder="Rest ECG (0-2)" required>
        <input type="number" name="thalach" placeholder="Max Heart Rate" required>
        <input type="number" name="exang" placeholder="Exercise Induced Angina (1=True, 0=False)" required>
        <input type="text" name="oldpeak" placeholder="Oldpeak" required>
        <input type="number" name="slope" placeholder="Slope (0-2)" required>
        <input type="number" name="ca" placeholder="Number of Major Vessels (0-3)" required>
        <input type="number" name="thal" placeholder="Thal (1-3)" required>
        <button type="submit">Predict</button>
    </form>
    {% if result %}
    <div class="result">
        <p><strong>{{ result }}</strong></p>
    </div>
    {% endif %}
</body>
</html>
"""

# =========================
# STEP 4: BACKEND ROUTES
# =========================
@app.route("/", methods=["GET"])
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/predict", methods=["POST"])
def predict():
    data = {key: request.form[key] for key in request.form}
    name = data["name"]

    features = [
        int(data["age"]), int(data["sex"]), int(data["cp"]),
        int(data["trestbps"]), int(data["chol"]), int(data["fbs"]),
        int(data["restecg"]), int(data["thalach"]), int(data["exang"]),
        float(data["oldpeak"]), int(data["slope"]), int(data["ca"]), int(data["thal"])
    ]

    X_input = scaler.transform([features])
    prediction = model.predict(X_input)[0]
    result_text = "❤️ Likely No Heart Disease" if prediction == 0 else "⚠️ High Risk of Heart Disease"

    # Store in database
    conn = sqlite3.connect("heart.db")
    c = conn.cursor()
    c.execute("INSERT INTO predictions (name, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, result) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (name, *features, result_text))
    conn.commit()
    conn.close()

    return render_template_string(HTML_TEMPLATE, result=result_text)

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)
