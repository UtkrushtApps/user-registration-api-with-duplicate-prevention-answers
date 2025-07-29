from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.models import Base, User
from app.schemas import UserCreate, UserOut
from app.database import engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/register", response_model=UserOut, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists at application level
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    new_user = User(email=user.email, name=user.name)
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered.")
    return new_user
