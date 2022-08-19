from ddd.domain.models.student import Student
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepo
from ddd.domain.service_abstraction.abstract_student_service import AbstractStudentService


class StudentService(AbstractStudentService):

    def __init__(self, student_repo: AbstractStudentRepo) -> None:
        self.student_repo = student_repo

    def insert_student(self, student: Student):
        """Add new student to database"""
        self.student_repo.add_record(student)
