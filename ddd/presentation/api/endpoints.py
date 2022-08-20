from fastapi import APIRouter
from container import Container
from ddd.application.student.commands.insert_student import InsertStudent
from ddd.application.student.queries.get_students import GetStudents
from ddd.domain.models.student import Student

router = APIRouter()
# student_service = Container.student_service()


@router.post("/students")
async def insert_student(stud: Student):
    # student_service.insert_student(stud)
    InsertStudent(stud, Container.student_repo())
    return "student Inserted Successfully!"


@router.get("/students")
async def get_students():
    return GetStudents(Container.student_repo()).students
