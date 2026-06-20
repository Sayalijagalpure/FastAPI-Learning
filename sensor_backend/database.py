from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base 
DATABASE_URL = "mysql+pymysql://root:admin1234@localhost/sensor_monitoring"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()