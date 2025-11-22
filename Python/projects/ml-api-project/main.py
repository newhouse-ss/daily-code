from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# @app: Initializes the FastAPI application instance
app = FastAPI(title="My First ML API")

if not os.path.exists("titanic_model.pkl"):
    raise RuntimeError("Model not found! Run train_model.py first.")
model = joblib.load("titanic_model.pkl")

class Passenger(BaseModel):
    pclass: int
    age: float
    fare: float

# @app.get("/"): Decorator to handle HTTP GET requests (retrieve data) at the root URL "/"
@app.get("/")
def home():
    return {"status": "running", "message": "Welcome to Titanic API"}

# @app.post("/predict"): Decorator to handle HTTP POST requests (submit data) at the URL "/predict"
@app.post("/predict")
def predict(passenger: Passenger):
    data = pd.DataFrame([passenger.model_dump()])
    
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    
    return {
        "survived_prediction": int(prediction),
        "survival_probability": round(float(probability), 4)
    }