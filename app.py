
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd

app=FastAPI(title="Air Quality Detection")

model=joblib.load("_air_quality_model.pkl")

class AirQualityInput(BaseModel):
    pm2_5: float
    pm10: float
    carbon_monoxide: float
    nitrogen_dioxide: float
    sulphur_dioxide: float
    ozone: float


@app.get("/")
def home():
    return{
        "message":"Welcome to Air Quality Detection"
    }

@app.post("/predict")
def predict(data : AirQualityInput):
  prediction=model.predict([[
      data.pm2_5,
      data.pm10,
      data.carbon_monoxide,
      data.nitrogen_dioxide,
      data.sulphur_dioxide,
      data.ozone
  ]])
  return{
      "prediction":prediction[0]
  }
