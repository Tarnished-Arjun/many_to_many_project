from sqlalchemy.orm import Session
from . import models


def create_student(db: Session, name: str):
    student = models.Student(name=name)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def create_course(db: Session, title: str):
    course = models.Course(title=title)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


def assign_courses(db: Session, student_id: int, course_ids: list[int]):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()

    if not student:
        return None

    courses = db.query(models.Course).filter(models.Course.id.in_(course_ids)).all()

    existing_ids = {c.id for c in student.courses}
    new_courses = [c for c in courses if c.id not in existing_ids]

    student.courses.extend(new_courses)

    db.commit()
    db.refresh(student)

    return student


def get_students(db: Session):
    return db.query(models.Student).all()


def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()


def get_courses(db: Session):
    return db.query(models.Course).all()


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


def delete_student(db: Session, student_id: int):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student


def delete_course(db: Session, course_id: int):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
    return course