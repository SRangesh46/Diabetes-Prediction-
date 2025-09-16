# 🩺 Diabetes Prediction System

The **Diabetes Prediction System** is a machine learning-based web application built using **Flask, Python, and Scikit-learn**.  
It predicts whether a patient is likely to have **Diabetes (Positive/Negative)** based on medical diagnostic data.  

The system leverages a **trained ML model (Logistic Regression / Random Forest / etc.)** stored in a `.pkl` file and provides predictions via a **web interface** and **REST API**.

---

## 📖 Background

Diabetes is one of the most common chronic diseases worldwide.  
Early detection and lifestyle modifications can help reduce severe complications.  
Machine learning provides a way to **analyze patient health records** and assist in **predicting diabetes risk**.

This project demonstrates how ML models can be integrated into **Flask web apps** for real-world applications.

---

## ✨ Features
- 🔮 **ML-powered Predictions**: Predicts diabetes based on health indicators.  
- 🌐 **Web Application**: User-friendly HTML frontend.  
- 📡 **REST API Endpoint**: Supports POST requests with JSON input.  
- 📦 **Model Integration**: Pre-trained model loaded with `joblib`.  
- 📊 **Dataset Compatibility**: Works with the famous **Pima Indians Diabetes Dataset**.  
- 💾 **Lightweight & Portable**: Can be run locally or deployed on the cloud.  

---

## 📂 Project Structure
Diabetes-Prediction-System/
│── app.py # Main Flask application
│── diabetes_model.pkl # Pre-trained ML model
│── templates/
│ └── index.html # Frontend HTML form
│── static/
│ └── style.css # (Optional) Styling for frontend
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── dataset/ # (Optional) Training dataset
│── train_model.ipynb # Notebook used for model training


---

🖥️ Usage
Web Interface

Open the homepage

Fill in details like:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

Click Predict

Get the result instantly on the page ✅
