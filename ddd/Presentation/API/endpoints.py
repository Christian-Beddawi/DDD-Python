from fastapi import APIRouter
from Container import Container

from ddd.Domain.Models.Student import Student

router = APIRouter()

student_service = Container.student_service()

@router.put("/students")
async def insert_student(stud: Student):
    student_service.insert_student(stud)
    # conn = engine.connect()
    # ins = students.insert().values(name=stud.first_name, lastname=stud.last_name)
    # result = conn.execute(ins)
    return "Student Inserted Successfully!"

