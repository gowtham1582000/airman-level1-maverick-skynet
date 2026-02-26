from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.core.security import hash_password, verify_password
from app.core.auth import create_access_token
from app.schemas.user import UserCreate
from app.core.dependencies import get_current_user, require_role

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email, "role": user.role})

    return {"access_token": token}

@router.get("/protected")
def protected(user = Depends(get_current_user)):
    return {"message": "Token valid", "user": user}

@router.get("/admin-only")
def admin_route(user = Depends(require_role("admin"))):
    return {"message": "Admin access granted"}