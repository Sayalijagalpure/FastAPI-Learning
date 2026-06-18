from pydantic import BaseModel

class ReadingCreate(BaseModel):
    device_id: int
    battery_percentage: int
    status: str