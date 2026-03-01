from pydantic import BaseModel
from typing import Optional

class SensorData(BaseModel):
    air_temperature_c: float
    soil_moisture_pct: float
    light_intensity_lux: Optional[float] = None

    nitrogen_ppm: Optional[float] = None
    phosphorus_ppm: Optional[float] = None
    potassium_ppm: Optional[float] = None
    soil_humidity_pct: Optional[float] = None
    soil_ph: Optional[float] = None


class SensorPayload(BaseModel):
    device_id: str
    plant_code: str
    recorded_at_epoch: Optional[int]
    sensor: SensorData

class NutrientTankData(BaseModel):
    distance_cm: float
    calculated_volume_ml: int
    tank_capacity_ml: int


class NutrientTankPayload(BaseModel):
    device_id: str
    measured_at_epoch: Optional[int]
    tank: NutrientTankData