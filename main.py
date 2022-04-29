from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from api import files

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(files.router)
# app.include_router(files.router) # for  future routers

if __name__ == '__main__':
  run("main:app", host="0.0.0.0", port=5000, reload=True)