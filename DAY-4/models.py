from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Reading(Base):

    __tablename__ = "readings"

    reading_id = Column(Integer, primary_key=True)
    device_id = Column(Integer)
    battery_percentage = Column(Integer)
    status = Column(String(20))