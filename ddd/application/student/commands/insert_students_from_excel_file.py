import shutil
import pandas as pd
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository


class InsertStudentsFromExcel:
    def __init__(self, students_file, student_repo: AbstractStudentRepository):
        try:
            with open(f"{students_file.filename}", 'wb') as buffer:
                shutil.copyfileobj(students_file.file, buffer)
        finally:
            students_file.file.close()
        df = pd.read_excel(students_file.filename)
        student_repo.add_multiple_students(df.to_dict("records"))
