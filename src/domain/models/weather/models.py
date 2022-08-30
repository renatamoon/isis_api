# STANDARD IMPORTS
from typing import Optional
from fastapi import Query
from pydantic import BaseModel, Extra


class CoordinatesModel(BaseModel):
    latitude: Optional[str] = Query(default=None)
    longitude: Optional[str] = Query(default=None)

    class Config:
        extra = Extra.forbid


class CityModel(BaseModel):
    city: Optional[str] = Query(default=None)

    class Config:
        extra = Extra.forbid
