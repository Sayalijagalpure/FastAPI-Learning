from fastapi import FastAPI
from database import SessionLocal
from models import Reading
from schemas import ReadingCreate

app = FastAPI()

@app.get("/readings")
def get_readings():

    db = SessionLocal()

    readings = db.query(Reading).all()

    return readings

@app.post("/readings")
def add_reading(reading: ReadingCreate):

    db = SessionLocal()

    new_reading = Reading(
        device_id=reading.device_id,
        battery_percentage=reading.battery_percentage,
        status=reading.status
    )

    db.add(new_reading)

    db.commit()

    return {
        "message": "Reading saved successfully"
    }