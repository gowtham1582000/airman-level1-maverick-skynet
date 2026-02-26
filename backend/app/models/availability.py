from sqlalchemy import Column, Integer, DateTime
from app.database import Base

class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True)
    instructor_id = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)