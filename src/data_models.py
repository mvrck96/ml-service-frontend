from typing import List

from pydantic import BaseModel


class TimeSeries(BaseModel):
    """Request data model"""

    feature: str
    data: List[float]
    smoothing_level: float
