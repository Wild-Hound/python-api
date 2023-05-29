from sqlalchemy.orm import Session
from sqlalchemy import exc
from model.urlModel import Url
from schemas.urlSchemas import UrlSchema
from datetime import datetime

import string
import random


def get_urls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Url).offset(skip).limit(limit).all()


def get_url_by_redirect(db: Session, redirect_url: str):
    return db.query(Url).filter(Url.redirect_url == redirect_url).first()


def get_redirect_url(db: Session, redirect_url: str):
    _url = get_url_by_redirect(db, redirect_url)

    if (_url.https):
        reconstructed_url = f"https://{_url.main_url}"
    else:
        reconstructed_url = f"http://{_url.main_url}"

    return reconstructed_url


def create_url(db: Session, url: UrlSchema):
    secure_url = True
    # generates a random string if redirect URL is not provided
    if (not url.redirect_url):
        url.redirect_url = ''.join(random.choices(string.ascii_uppercase +
                                                  string.digits, k=8))

    # strips "http://" or "https://" out of the main URL
    if (url.main_url.startswith("http://") or url.main_url.startswith("https://")):
        # sets "https" column in DB to false if the main URL is http by using "secure_url" variable
        if url.main_url.startswith("http://"):
            url.main_url = url.main_url.replace("http://", "")
            secure_url = False
        else:
            url.main_url = url.main_url.replace("https://", "")

    try:
        _url = Url(
            main_url=url.main_url,
            redirect_url=url.redirect_url,
            views=0,
            edits=0,
            created=datetime.now(),
            https=secure_url
        )
        db.add(_url)
        db.commit()
        db.refresh(_url)
        return _url

    except exc.IntegrityError as e:
        print("hello", e.__dict__["orig"])
