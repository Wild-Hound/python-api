from fastapi import FastAPI
import model.bookModel as bookModel
from config.bookConfig import engine
from router.bookRouter import router

bookModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def home():
    return "Hello World"

app.include_router(router, prefix="/book", tags=["book"])
