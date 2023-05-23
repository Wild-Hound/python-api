from sqlalchemy.orm import Session
from sqlalchemy import exc
from model.urlModel import Url
from schemas.urlSchemas import UrlSchema
from datetime import datetime

import string
import random


def get_urls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Url).offset(skip).limit(limit).all()


def get_url_by_main(db: Session, main_url: int):
    return db.query(Url).filter(Url.main_url == main_url).first()


def get_url_by_redirect(db: Session, redirect_url: int):
    return db.query(Url).filter(Url.redirect_url == redirect_url).first()


def create_url(db: Session, url: UrlSchema):

    if (not url.redirect_url):
        url.redirect_url = ''.join(random.choices(string.ascii_uppercase +
                                                  string.digits, k=8))

    if (url.main_url.startswith("http://") or url.main_url.startswith("https://")):
        url.main_url = url.main_url.replace("http://", "")
        url.main_url = url.main_url.replace("https://", "")

    try:
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

    except exc.IntegrityError as e:
        e = str(e)
        detail_start = e.find("DETAIL:") + len("DETAIL:")
        detail_end = e.find("\n", detail_start)

        detail_value = e[detail_start:detail_end].strip()
        print(detail_value)
        print(e)

        return detail_value
    
