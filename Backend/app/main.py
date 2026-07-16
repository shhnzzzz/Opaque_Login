from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import db

from app.routers.auth_router import router as auth_router
from app.routers.login_router import router as login_router

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome to OPAQUE Authentication API"}

@app.get("/hello")
def hello():
    return {"message": "Hello React! Welcome to OPAQUE Authentication."}

@app.get("/database-test")
async def database_test():
    collections = await db.list_collection_names()

    return {
        "database": "Connected!",
        "collections": collections
    }



app.include_router(auth_router)

app.include_router(login_router)