from fastapi import FastAPI
from .database import engine, Base
from app.routes import student, course

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student.router)
app.include_router(course.router)


@app.get("/")
def home():
    return {"message": "Many-to-Many API Running"}