from fastapi import FastAPI
from core.config import settings
from database.db import engine, Base
from models.User.router import router as UserRouter

from fastapi.middleware.cors import CORSMiddleware


# Table creation
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.app_name,
)

app.include_router(UserRouter)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"Hello": "World ", "appName": settings.app_name}
