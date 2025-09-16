from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the trained model
model = joblib.load("diabetes_model.pkl")

# Define feature columns
feature_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = pd.DataFrame([data], columns=feature_columns)
        prediction = model.predict(input_data)[0]
        result = "Diabetes" if prediction == 1 else "No Diabetes"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
