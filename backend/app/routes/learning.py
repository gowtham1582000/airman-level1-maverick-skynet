from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.course import Course
from app.models.lesson import Lesson
from app.models.module import Module
from app.models.quiz_attempt import QuizAttempt
from app.core.dependencies import require_role

router = APIRouter(prefix="/learning", tags=["Learning"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Course (Instructor only)
@router.post("/courses")
def create_course(
    title: str,
    description: str,
    db: Session = Depends(get_db),
    user = Depends(require_role("instructor"))
):

    course = Course(title=title, description=description)

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


# List Courses (Pagination + Search)
@router.get("/courses")
def list_courses(
    search: str = "",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Course)

    if search:
        query = query.filter(Course.title.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()

# Create Module (Instructor only)
@router.post("/courses/{course_id}/modules")
def create_module(
    course_id: int,
    title: str,
    db: Session = Depends(get_db),
    user = Depends(require_role("instructor"))
):

    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    module = Module(title=title, course_id=course_id)

    db.add(module)
    db.commit()
    db.refresh(module)

    return module

@router.get("/courses/{course_id}/modules")
def list_modules(
    course_id: int,
    db: Session = Depends(get_db)
):

    modules = db.query(Module).filter(Module.course_id == course_id).all()

    return modules

@router.post("/modules/{module_id}/lessons")
def create_lesson(
    module_id: int,
    title: str,
    type: str,
    content: dict,
    db: Session = Depends(get_db),
    user = Depends(require_role("instructor"))
):

    module = db.query(Module).filter(Module.id == module_id).first()

    if not module:
        raise HTTPException(status_code=404, detail="Module not found")

    if type not in ["text", "quiz"]:
        raise HTTPException(status_code=400, detail="Invalid lesson type")

    lesson = Lesson(
        title=title,
        type=type,
        content=content,
        module_id=module_id
    )

    db.add(lesson)
    db.commit()
    db.refresh(lesson)

    return lesson

@router.get("/modules/{module_id}/lessons")
def list_lessons(
    module_id: int,
    db: Session = Depends(get_db)
):

    lessons = db.query(Lesson).filter(Lesson.module_id == module_id).all()

    return lessons