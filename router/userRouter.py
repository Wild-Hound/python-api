from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.slowConfig import SessionLocal
from sqlalchemy.orm import Session
from schemas.userSchemas import Response, RequestUser
import crud.userCrud as userCrud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_user_service(request: RequestUser, db: Session = Depends(get_db)):
    userCrud.create_user(db, user=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="User created successfully").dict(exclude_none=True)

@router.get("/")
async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _users = userCrud.get_users(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)


@router.get("/{email}")
async def get_users(email: str, db: Session = Depends(get_db)):
    _users = userCrud.get_user_by_email(db, email)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_users)