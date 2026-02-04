from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.db import engine
from app.models import Plant, Device, SensorReadingRaw
from app.schemas import SensorPayload

app = FastAPI(title="IoT Salak Sensor API")

def get_utc_time(epoch: int | None):
    if epoch:
        return datetime.fromtimestamp(epoch, tz=timezone.utc)
    return datetime.now(timezone.utc)


def check_validity(sensor):
    if sensor.air_temperature_c >= 85:
        return False
    if sensor.soil_moisture_pct <= 0 or sensor.soil_moisture_pct > 100:
        return False
    if sensor.soil_ph and (sensor.soil_ph < 3 or sensor.soil_ph > 9):
        return False
    return True


@app.post("/api/v1/sensor-reading")
def ingest_sensor(payload: SensorPayload):
    with Session(engine) as session:
        plant = session.query(Plant).filter_by(
            plant_code=payload.plant_code
        ).first()
        if not plant:
            raise HTTPException(404, "Plant not found")

        device = session.query(Device).filter_by(
            device_code=payload.device_id
        ).first()
        if not device:
            raise HTTPException(404, "Device not found")

        recorded_at = get_utc_time(payload.recorded_at_epoch)
        is_valid = check_validity(payload.sensor)

        reading = SensorReadingRaw(
            plant_id=plant.plant_id,
            device_id=device.device_id,
            recorded_at=recorded_at,

            air_temperature_c=payload.sensor.air_temperature_c,
            soil_moisture_pct=payload.sensor.soil_moisture_pct,
            light_intensity_lux=payload.sensor.light_intensity_lux,

            nitrogen_ppm=payload.sensor.nitrogen_ppm,
            phosphorus_ppm=payload.sensor.phosphorus_ppm,
            potassium_ppm=payload.sensor.potassium_ppm,
            soil_humidity_pct=payload.sensor.soil_humidity_pct,
            soil_ph=payload.sensor.soil_ph,

            is_valid=is_valid
        )

        session.add(reading)
        session.commit()

    return {
        "status": "ok",
        "is_valid": is_valid,
        "server_time": datetime.now(timezone.utc).isoformat()
    }