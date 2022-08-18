from ddd.Domain.RepositoryAbstraction.AbstractStudentRepo import AbstractStudentRepo
from ddd.Domain.ServiceAbstraction.AbstractStudentService import AbstractStudentService
from ddd.Domain.Models import Student


class StudentService(AbstractStudentService):

    def __init__(self, student_repo: AbstractStudentRepo) -> None:
        super().__init__()
        self.student_repo = student_repo

    def insert_student(self, student: Student):
        """Add new student to database"""
        self.student_repo.add_record(student)
        pass
