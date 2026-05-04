from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/courses", tags=["Courses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_course(data: schemas.CourseCreate, db: Session = Depends(get_db)):
    return crud.create_course(db, data.title)


@router.get("/", response_model=list[schemas.CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db)


@router.get("/{course_id}", response_model=schemas.CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return crud.get_course(db, course_id)


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    return crud.delete_course(db, course_id)