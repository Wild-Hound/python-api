from sqlalchemy.orm import Session
from model.urlModel import Url
from schemas.urlSchemas import UrlSchema
from datetime import datetime


def get_urls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Url).offset(skip).limit(limit).all()


def get_url_by_main(db: Session, main_url: int):
    return db.query(Url).filter(Url.main_url == main_url).first()


def get_url_by_redirect(db: Session, redirect_url: int):
    return db.query(Url).filter(Url.redirect_url == redirect_url).first()


def create_url(db: Session, url: UrlSchema):
    _url = Url(
        main_url=url.main_url,
        redirect_url=url.redirect_url,
        views=0,
        edits=0,
        created=datetime.now()
    )
    db.add(_url)
    db.commit()
    db.refresh(_url)
    return _url
