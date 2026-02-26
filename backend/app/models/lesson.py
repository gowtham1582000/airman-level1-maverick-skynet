# app/models/lesson.py
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

    type = Column(String)  # "text" or "quiz"
    content = Column(JSON) # stores text or quiz questions

    module_id = Column(Integer, ForeignKey("modules.id"))

    module = relationship("Module", back_populates="lessons")