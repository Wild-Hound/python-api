from fastapi import APIRouter, Response as FastResponse
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
async def create_url(request: RequestUrl, response: FastResponse, db: Session = Depends(get_db)):
    res = urlCrud.create_url(db, url=request.parameter)
    if not res:
        response.status_code = 400
        return Response(code="200", message="exists").dict(exclude_none=True)
    return Response(
        code="200",
        message="Url created successfully",
        result=res
    ).dict(exclude_none=True)


@router.get("/all")
async def get_urls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _urls = urlCrud.get_urls(db, skip, limit)
    return Response(code="200", message="Success fetch all data", result=_urls)


@router.get("/{redirect_url}")
async def get_redirect_url(redirect_url: str, response: FastResponse, db: Session = Depends(get_db)):
    _url = urlCrud.get_redirect_url(db, redirect_url)
    print(_url, redirect_url)
    response.status_code = 307
    response.headers['Location'] = _url
    return Response(code="307", message="Success fetch all data", result=_url)
