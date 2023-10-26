from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.board import board_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://localhost:3000",
    "*/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(board_router.router)
app.include_router(user_router.router)

# uvicorn main:app --reload