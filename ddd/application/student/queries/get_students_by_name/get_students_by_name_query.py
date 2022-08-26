from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository


class GetStudentsByNameQuery:

    def __init__(self, name, student_repo: AbstractStudentRepository):
        self.student_repo = student_repo
        self.name = name
        # self.students = student_repo.get_all_students()
