import shutil
import pandas as pd
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from mediatr import Mediator


class InsertStudentsFromExcelCommand:
    def __init__(self, students_file, student_repo: AbstractStudentRepository):
        self.students_file = students_file
        self.student_repo = student_repo


@Mediator.handler
class InsertStudentCommandHandler:
    def handle(self, request: InsertStudentsFromExcelCommand):
        try:
            with open(f"{request.students_file.filename}", 'wb') as buffer:
                shutil.copyfileobj(request.students_file.file, buffer)
        finally:
            request.students_file.file.close()
        df = pd.read_excel(request.students_file.filename)
        request.student_repo.add_multiple_students(df.to_dict("records"))
