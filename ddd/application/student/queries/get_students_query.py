from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from mediatr import Mediator


class GetStudentsQuery:

    def __init__(self, student_repo: AbstractStudentRepository):
        self.student_repo = student_repo
        # self.students = student_repo.get_all_students()


@Mediator.handler
class GetStudentsQueryHandler:
    def handle(self, request: GetStudentsQuery):
        return request.student_repo.get_all_students()
