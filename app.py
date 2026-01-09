from fastapi import FastAPI
import pickle
import pandas as pd

# Create FastAPI app
app = FastAPI(title="Telco Customer Churn Prediction API")

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load encoders (VERY IMPORTANT)
encoders = pickle.load(open("encoders.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Telco Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(data: dict):

    # Convert input JSON to DataFrame
    input_df = pd.DataFrame([data])

    # Encode categorical columns
    for col, encoder in encoders.items():
        input_df[col] = encoder.transform(input_df[col])

    # Make prediction
    prediction = model.predict(input_df)[0]

    result = "Churn" if prediction == 1 else "No Churn"

    return {
        "prediction": int(prediction),
        "result": result
    }
