import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model = joblib.load(BASE_DIR / "model/rf_model_final.pkl")
label_encoder = joblib.load(BASE_DIR / "model/label_encoder.pkl")

def predict_wqi(data):
    features = np.array([[
        data.ammonia,
        data.bod,
        data.do,
        data.orthophosphate,
        data.ph,
        data.temperature,
        data.nitrogen,
        data.nitrate
    ]])

    prediction = model.predict(features)

    return label_encoder.inverse_transform(prediction)[0]