import joblib
from fastapi import FastAPI
import pandas as pd
from src.feature_pipeline import preprocess_input
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "best_model.pkl"

# Load model
model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {"message": "House Price Prediction API is running"}


@app.post("/predict")
def predict(data: dict):

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # Apply preprocessing
    df = preprocess_input(df)

    # Predict
    prediction = model.predict(df)

    # LOG INPUT + OUTPUT
    logging.info(f"Input: {data}")
    logging.info(f"Prediction: {prediction[0]}")

    return {"predicted_price": float(prediction[0])}
