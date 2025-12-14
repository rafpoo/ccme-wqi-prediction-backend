from pydantic import BaseModel

class WqiRequest(BaseModel):
    ammonia: float
    bod: float
    do: float
    orthophosphate: float
    ph: float
    temperature: float
    nitrogen: float
    nitrate: float

class WqiResponse(BaseModel):
    prediction: str