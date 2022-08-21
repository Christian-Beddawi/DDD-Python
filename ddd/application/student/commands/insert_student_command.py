from ddd.domain.models.student import Student
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from mediatr import Mediator


class InsertStudentCommand:

    def __init__(self, student: Student, student_repo: AbstractStudentRepository) -> None:
        self.student_repo = student_repo
        self.student = student


@Mediator.handler
class InsertStudentCommandHandler:
    def handle(self, request: InsertStudentCommand):
        request.student_repo.add_student(request.student)
