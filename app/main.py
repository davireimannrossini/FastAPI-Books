from typing import Union
from fastapi import FastAPI
import model
from config import engine
import app.router as router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def Home():
    return {"Welcome Home"}

app.include_router(router.router, prefix="/book", tags=["book"])
