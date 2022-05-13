from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware

from api import files, users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DOPS Backend",
    discription="Drawing Office Processing System",
    version="0.0.1",
    contact={"name": "Elvin", "email": "ebashirli@hotmail.com"},
    license_info={"name": "MIT"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(files.router)
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

if __name__ == "__main__":
    # run("main:app", host="0.0.0.0", port=5000, reload=True)
    run("main:app", reload=True)
