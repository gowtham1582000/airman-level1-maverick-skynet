# app/models/quiz_attempt.py
from sqlalchemy import Column, Integer, ForeignKey, JSON
from app.database import Base

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, index=True)

    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    student_id = Column(Integer, ForeignKey("users.id"))

    score = Column(Integer)
    answers = Column(JSON)