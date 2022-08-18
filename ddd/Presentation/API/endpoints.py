from fastapi import APIRouter
from Container import Container

from ddd.Domain.Models.Student import Student

router = APIRouter()

student_service = Container.student_service()

@router.put("/students")
async def insert_student(stud: Student):
    student_service.insert_student(stud)
    return "Student Inserted Successfully!"

