import uvicorn
from fastapi import FastAPI
from mediatr import Mediator
from container import Container
from ddd.application.middleware.logging_middleware import LoggingMiddleware
from ddd.application.student.commands.insert_student.insert_student_comand_handler import InsertStudentCommandHandler
from ddd.application.student.commands.insert_students_from_excel.insert_students_from_excel_file_command_handler import \
    InsertStudentFromExcelCommandHandler
from ddd.application.student.queries.get_students.get_students_query_handler import GetStudentsQueryHandler
from ddd.application.student.queries.get_students_by_name.get_students_by_name_query_handler import \
    GetStudentsByNameQueryHandler
from ddd.application.student.queries.get_students_excel_file.get_students_excel_file_query_handler import \
    GetStudentsExcelQueryHandler
from ddd.presentation.api import students_controller


container = Container()
app = FastAPI()
app.container = container
app.include_router(students_controller.router)

# Middleware Registration
app.add_middleware(LoggingMiddleware)

# Request Handlers Registration
Mediator.register_handler(GetStudentsQueryHandler)
Mediator.register_handler(GetStudentsExcelQueryHandler)
Mediator.register_handler(InsertStudentCommandHandler)
Mediator.register_handler(InsertStudentFromExcelCommandHandler)
Mediator.register_handler(GetStudentsByNameQueryHandler)

if __name__=="__main__":
    uvicorn.run(app=app)
