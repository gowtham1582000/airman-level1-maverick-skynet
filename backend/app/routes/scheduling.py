from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import SessionLocal
from app.models.booking import Booking
from app.core.dependencies import require_role
from app.models.availability import Availability

router = APIRouter(prefix="/schedule", tags=["Scheduling"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/book")
def create_booking(
    instructor_id: int,
    start_time: datetime,
    end_time: datetime,
    db: Session = Depends(get_db),
    user = Depends(require_role("student"))
):

    conflict = db.query(Booking).filter(
        Booking.instructor_id == instructor_id,
        Booking.start_time < end_time,
        Booking.end_time > start_time,
        Booking.status != "rejected"
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Booking conflict detected"
        )

    booking = Booking(
        instructor_id=instructor_id,
        student_id=user["email"],
        start_time=start_time,
        end_time=end_time
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking


@router.put("/booking/{booking_id}/approve")
def approve_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_role("admin"))
):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.status = "approved"

    db.commit()
    db.refresh(booking)

    return booking

@router.put("/booking/{booking_id}/reject")
def reject_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    user = Depends(require_role("instructor"))
):

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    booking.status = "rejected"

    db.commit()

    return {"message": "Booking rejected"}

@router.post("/availability")
def create_availability(
    start_time: datetime,
    end_time: datetime,
    db: Session = Depends(get_db),
    user = Depends(require_role("instructor"))
):

    slot = Availability(
        instructor_id=user["id"],
        start_time=start_time,
        end_time=end_time
    )

    db.add(slot)
    db.commit()
    return slot

from datetime import timedelta

@router.get("/calendar/week")
def weekly_calendar(
    instructor_id: int,
    start: datetime,
    db: Session = Depends(get_db)
):

    end = start + timedelta(days=7)

    bookings = db.query(Booking).filter(
        Booking.instructor_id == instructor_id,
        Booking.start_time >= start,
        Booking.start_time <= end
    ).all()

    return bookings