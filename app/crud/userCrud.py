from sqlalchemy.orm import Session
from model.userModel import User
from schemas.userSchemas import UserSchema
from datetime import datetime


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserSchema):
    _user = User(email=user.email, password=user.password, full_name=user.full_name, age=user.age, created=datetime.now())
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user