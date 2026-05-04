from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas

router = APIRouter(prefix="/students", tags=["Students"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_student(data: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, data.name)


@router.get("/", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@router.get("/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)


@router.post("/assign/")
def assign_courses(data: schemas.AssignCourses, db: Session = Depends(get_db)):
    return crud.assign_courses(db, data.student_id, data.course_ids)


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)