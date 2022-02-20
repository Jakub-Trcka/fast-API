
# uvicorn app.main:app --reload
# 11:08:00 1




from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, ath, vote
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(ath.router)
app.include_router(vote.router)


# welcome sing
@app.get("/")
def welcome():
    return {'message': 'Welcome to my api'}





