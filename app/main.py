from fastapi import FastAPI

import model.bookModel as bookModel
import model.userModel as userModel

from config.bookConfig import engine as bookEngine
from config.slowConfig import engine as slowEngine

from router.bookRouter import router as bookRouter
from router.userRouter import router as userRouter

bookModel.Base.metadata.create_all(bind=bookEngine)
userModel.Base.metadata.create_all(bind=slowEngine)

app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"

app.include_router(bookRouter, prefix="/book", tags=["book"])
app.include_router(userRouter, prefix="/user", tags=["user"])
