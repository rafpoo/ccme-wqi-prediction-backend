from fastapi import FastAPI
from app.schemas import WqiRequest, WqiResponse
from app.services.predictor import predict_wqi

app = FastAPI(
    title="WQI Prediction API",
    description="An API to predict Water Quality Index (WQI) based on water quality parameters.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "WQI API is running 🚀"}

@app.post("/predict", response_model=WqiResponse)
def predict(request: WqiRequest):
    result = predict_wqi(request)
    return WqiResponse(prediction=result)
