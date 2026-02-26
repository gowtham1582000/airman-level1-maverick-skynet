from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.routes import auth
from app.models.course import Course
from app.models.module import Module
from app.models.lesson import Lesson
from app.models.quiz_attempt import QuizAttempt
from app.routes import learning
from app.models.booking import Booking
from app.routes import scheduling
from app.models.availability import Availability

app = FastAPI()
app.include_router(auth.router)
app.include_router(learning.router)
Base.metadata.create_all(bind=engine)
app.include_router(scheduling.router)

@app.get("/")
def home():
    return {"message": "Database connected successfully"}