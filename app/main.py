
from fastapi import FastAPI
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
    return 'Welcome to my. If you want more userfriendly experience, then type after our URL /docs'




