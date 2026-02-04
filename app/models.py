from sqlalchemy import Column, Integer, String, Boolean, Numeric, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Plant(Base):
    __tablename__ = "plant"
    __table_args__ = {"schema": "raw"}

    plant_id = Column(Integer, primary_key=True)
    plant_code = Column(String, unique=True)


class Device(Base):
    __tablename__ = "device"
    __table_args__ = {"schema": "raw"}

    device_id = Column(Integer, primary_key=True)
    device_code = Column(String, unique=True)
    plant_id = Column(Integer, ForeignKey("raw.plant.plant_id"))


class SensorReadingRaw(Base):
    __tablename__ = "sensor_reading_raw"
    __table_args__ = {"schema": "raw"}

    reading_id = Column(Integer, primary_key=True)
    plant_id = Column(Integer)
    device_id = Column(Integer)

    recorded_at = Column(TIMESTAMP(timezone=True), nullable=False)

    air_temperature_c = Column(Numeric(5,2))
    soil_moisture_pct = Column(Numeric(5,2))
    light_intensity_lux = Column(Numeric(10,2))

    nitrogen_ppm = Column(Numeric(10,2))
    phosphorus_ppm = Column(Numeric(10,2))
    potassium_ppm = Column(Numeric(10,2))
    soil_humidity_pct = Column(Numeric(5,2))
    soil_ph = Column(Numeric(4,2))

    is_valid = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())