from fastapi import FastAPI

import model.bookModel as bookModel
import model.userModel as userModel
import model.urlModel as urlModel

from config.bookConfig import engine as bookEngine
from config.slowConfig import engine as slowEngine
from config.url_shortenerConfig import engine as url_shortenerEngine

from router.bookRouter import router as bookRouter
from router.userRouter import router as userRouter
from router.urlRouter import router as urlRouter

bookModel.Base.metadata.create_all(bind=bookEngine)
userModel.Base.metadata.create_all(bind=slowEngine)
urlModel.Base.metadata.create_all(bind=url_shortenerEngine)

app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"

app.include_router(bookRouter, prefix="/book", tags=["book"])
app.include_router(userRouter, prefix="/user", tags=["user"])
app.include_router(urlRouter, prefix="/url_shortener", tags=["url"])
