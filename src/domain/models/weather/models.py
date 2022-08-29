# STANDARD IMPORTS
from typing import Optional
from fastapi import Query
from pydantic import BaseModel, validator


class CoordinatesModel(BaseModel):
    latitude: Optional[str] = Query(default=None)
    longitude: Optional[str] = Query(default=None)


class CityModel(BaseModel):
    city: Optional[str] = Query(default=None)
