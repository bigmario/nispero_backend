from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from sqlalchemy.orm import Session

from app.modules.subscriptions.controller import subscriptions_router
from app.modules.mail.controller import email_router

from app.core.database import create_db


app = FastAPI()
app.title = "Nispero Subscription Management API V3"
app.description = """
    API developed with FastAPI for Nispero
    Trienlace <trienlace@gmail.com>
    Mario Castro <mariocastro.pva@gmail.com>"""

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(subscriptions_router)
app.include_router(email_router)


@app.on_event("startup")
async def start_db():
    create_db()


@app.get(path="/", summary="Index", tags=["Index"], status_code=status.HTTP_200_OK)
async def index():
    return JSONResponse(
        {
            "Framework": "FastAPI",
            "Message": "Welcome To Nispero API !!",
        }
    )


add_pagination(app)
