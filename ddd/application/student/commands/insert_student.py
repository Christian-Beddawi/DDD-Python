from ddd.domain.models.student import Student
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository


class InsertStudent:

    def __init__(self, student: Student, student_repo: AbstractStudentRepository) -> None:
        self.student_repo = student_repo
        self.student_repo.add_student(student)
