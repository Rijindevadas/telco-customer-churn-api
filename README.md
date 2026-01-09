# telco-customer-churn-api
Customer churn prediction using ML and FastAPI

Telco Customer Churn Prediction API
Overview

This project implements an end-to-end machine learning solution to predict customer churn in a telecom company. The objective is to identify customers who are likely to discontinue the service based on their demographic details, account information, and service usage patterns.

The project covers the complete workflow, including data preprocessing, model training and evaluation, and deployment of the trained model as a REST API using FastAPI.


Problem Statement
Customer churn is a critical business problem in the telecom industry. Predicting churn in advance allows companies to take proactive steps such as targeted offers or service improvements to retain customers and reduce revenue loss.

Dataset
Name: Telco Customer Churn Dataset
Type: Structured (tabular) data
Target Variable: Churn
Features:
Customer demographics
Subscription and service details
Billing and payment information

Solution Approach
Data Preprocessing
Handled missing values in numerical and categorical columns
Encoded categorical features using label encoding
Ensured consistency between training and inference data
Prepared a clean dataset suitable for model training

Model Development
Trained and evaluated classification models
Selected the final model based on performance metrics
Evaluation metrics used:
Accuracy
Precision
Recall
F1-score

Model Persistence
Serialized the trained model using pickle
Saved preprocessing encoders separately to maintain consistency during prediction


API Development
Built a RESTful API using FastAPI
The API:
Accepts customer data in JSON format
Applies the same preprocessing steps used during training
Returns churn prediction as a JSON response
Input validation is handled using Pydantic models




API Endpoints
Health Check

GET /

{
  "message": "Telco Churn Prediction API is running"
}

-------------------------------------------------------------

Predict Churn

POST /predict

Sample Request:

{
  "gender": "Male",
  "SeniorCitizen": 0,
  "Partner": "Yes",
  "Dependents": "No",
  "tenure": 12,
  "PhoneService": "Yes",
  "InternetService": "Fiber optic",
  "MonthlyCharges": 75.5,
  "TotalCharges": 900.3
}

-------------------------------------------------------------------

Sample Response:

{
  "prediction": 1,
  "result": "Churn"
}

----------------------------------------------------



├── app.py                  # FastAPI application
├── main.ipynb              # Data preprocessing and model training
├── cleaned_data.csv        # Processed dataset
├── model.pkl               # Trained ML model
├── encoders.pkl            # Saved encoders for categorical features
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation


How to Run the Project==>>>
Clone or download the repository
Install required dependencies:
pip install -r requirements.txt
Start the FastAPI server:
uvicorn app:app --reload
Open the API documentation in your browser:
http://127.0.0.1:8000/docs





Technologies Used
Python
Pandas, NumPy
Scikit-learn
FastAPI
Uvicorn


Future Enhancements
Better handling of unseen categorical values
Hyperparameter tuning for improved performance
Model monitoring and periodic retraining
Cloud deployment for public access



Conclusion   ::
---------------
This project demonstrates a practical implementation of a machine learning system with a strong emphasis on clean data handling, model evaluation, and production-ready deployment. It reflects real-world ML engineering practices beyond just training a model.
