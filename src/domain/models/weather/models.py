# STANDARD IMPORTS
from typing import Optional
from pydantic import BaseModel


class CoordinatesModel(BaseModel):
    latitude: Optional[str] = None
    longitude: Optional[str] = None


class CityModel(BaseModel):
    city: Optional[str] = None
