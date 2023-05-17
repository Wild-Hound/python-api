from fastapi import FastAPI

import model.bookModel as bookModel
import model.userModel as userModel

from config.bookConfig import engine as bookEngine
from config.slowConfig import engine as slowEngine

from router.bookRouter import router

bookModel.Base.metadata.create_all(bind=bookEngine)
userModel.Base.metadata.create_all(bind=slowEngine)

app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"

app.include_router(router, prefix="/book", tags=["book"])
