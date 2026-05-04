from pydantic import BaseModel
from typing import List


class CourseBase(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    name: str

class CourseCreate(BaseModel):
    title: str

class StudentResponse(StudentBase):
    courses: List[CourseBase] = []


class CourseResponse(CourseBase):
    students: List[StudentBase] = []