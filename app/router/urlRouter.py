from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.url_shortenerConfig import SessionLocal
from sqlalchemy.orm import Session
from schemas.urlSchemas import Response, RequestUrl
import crud.urlCrud as urlCrud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_url(request: RequestUrl, db: Session = Depends(get_db)):
    urlCrud.create_url(db, url=request.parameter)
    return Response(
        code="200",
        message="Url created successfully").dict(exclude_none=True)


@router.get("/")
async def get_urls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _urls = urlCrud.get_urls(db, skip, limit)
    return Response(code="200", message="Success fetch all data", result=_urls)


@router.get("/main/{main_url}")
async def get_main_url(main_url: str, db: Session = Depends(get_db)):
    _url = urlCrud.get_url_by_main(db, main_url)
    return Response(code="200", message="Success fetch all data", result=_url)


@router.get("/redirect/{redirect_url}")
async def get_main_url(redirect_url: str, db: Session = Depends(get_db)):
    _url = urlCrud.get_url_by_main(db, redirect_url)
    return Response(code="200", message="Success fetch all data", result=_url)