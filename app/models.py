# Pydantic models for request/response validation
from pydantic import BaseModel
from typing import Optional

class PredictionInput(BaseModel):
    PC1: float
    PC2: float
    PC3: float
    ra: float
    dec: float
    j_mag: float
    h_mag: float
    k_mag: float
    kep_mag: float
    planet_radius: float
    orbital_period: float
    star_teff: float
    star_logg: float
    star_radius: float
    star_mass: float
    lc_time0: float

class PredictionResponse(BaseModel):
    prediction: int
    confidence: float
    class_name: str