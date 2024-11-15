# app.py
from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict/")
def predict(data: list):
    prediction = model.predict(np.array(data))
    return {"prediction": prediction.tolist()}
