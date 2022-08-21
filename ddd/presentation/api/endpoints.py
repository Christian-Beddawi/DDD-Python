from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from openpyxl.utils.exceptions import InvalidFileException

from container import Container
from ddd.application.student.commands.insert_student import InsertStudent
from ddd.application.student.commands.insert_students_from_excel_file import InsertStudentsFromExcel
from ddd.application.student.queries.get_students import GetStudents
from ddd.application.student.queries.get_students_excel_file import GetStudentsExcel
from ddd.domain.models.student import Student
from openpyxl import load_workbook

router = APIRouter()


# student_service = Container.student_service()


@router.post("/students")
async def insert_student(stud: Student):
    # student_service.insert_student(stud)
    InsertStudent(stud, student_repo=Container.student_repo())
    return "student Inserted Successfully!"


@router.post("/students/upload/")
async def insert_students_from_excel(students_file: UploadFile):
    try:
        load_workbook(students_file.filename)
    except InvalidFileException as e:
        return "Unsupported file type!!"
    InsertStudentsFromExcel(students_file, student_repo=Container.student_repo())
    return "Students added successfully to database!"


@router.get("/students")
async def get_students():
    return GetStudents(Container.student_repo()).students


@router.get("/students/download/{excel_file_name}")
async def get_students_excel_file(excel_file_name: str):
    GetStudentsExcel(excel_file_name=excel_file_name, student_repo=Container.student_repo())
    headers = {'Content-Disposition': 'attachment; filename="students.xlsx"'}
    return FileResponse("students.xlsx", headers=headers)
