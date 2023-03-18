from typing import List

from pydantic import BaseModel

class TimeSeries(BaseModel):
    feature: str
    data: List[float]
    smoothing_level: float

class PredictedValue(BaseModel):
    feature: str
    predicted_value: float
    