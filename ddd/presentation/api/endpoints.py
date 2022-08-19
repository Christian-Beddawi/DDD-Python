from fastapi import APIRouter
from container import Container

from ddd.domain.models.student import Student

router = APIRouter()
student_service = Container.student_service()


@router.post("/students")
async def insert_student(stud: Student):
    student_service.insert_student(stud)
    return "Student Inserted Successfully!"
