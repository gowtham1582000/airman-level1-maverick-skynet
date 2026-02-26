from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    instructor_id = Column(Integer)
    student_id = Column(String)

    start_time = Column(DateTime)
    end_time = Column(DateTime)

    status = Column(String, default="pending")