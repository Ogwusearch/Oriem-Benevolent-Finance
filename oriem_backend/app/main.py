from fastapi import FastAPI
from app.routers import auth_router
from app.database import Base, engine

app = FastAPI(title="ORiem Banking API", version="1.0")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
