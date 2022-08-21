from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from openpyxl.utils.exceptions import InvalidFileException
from container import Container
from ddd.application.student.commands.insert_student_command import InsertStudentCommand
from ddd.application.student.commands.insert_students_from_excel_file_command import InsertStudentsFromExcelCommand
from ddd.application.student.queries.get_students_query import GetStudentsQuery
from ddd.application.student.queries.get_students_excel_file_query import GetStudentsExcelQuery
from ddd.domain.models.student import Student
from openpyxl import load_workbook
from mediatr import Mediator

router = APIRouter()

# student_service = Container.student_service()
mediator = Mediator()


@router.post("/students")
async def insert_student(stud: Student):
    # student_service.insert_student(stud)
    await mediator.send_async(InsertStudentCommand(stud, student_repo=Container.student_repo()))
    return "student Inserted Successfully!"


@router.post("/students/upload/")
async def insert_students_from_excel(students_file: UploadFile):
    try:
        load_workbook(students_file.filename)
    except InvalidFileException as e:
        return "Unsupported file type!!"
    await mediator.send_async(InsertStudentsFromExcelCommand(students_file, student_repo=Container.student_repo()))
    return "Students added successfully to database!"


@router.get("/students")
async def get_students():
    # return GetStudentsQuery(Container.student_repo()).students
    return await mediator.send_async(GetStudentsQuery(Container.student_repo()))


@router.get("/students/download/{excel_file_name}")
async def get_students_excel_file(excel_file_name: str):
    await mediator.send_async(GetStudentsExcelQuery(excel_file_name=excel_file_name, student_repo=Container.student_repo()))
    headers = {'Content-Disposition': 'attachment; filename="students.xlsx"'}
    return FileResponse(excel_file_name + ".xlsx", headers=headers)
