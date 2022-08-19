from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository


class GetStudents:

    def __init__(self, student_repo: AbstractStudentRepository):
        self.student_repo = student_repo
        self.students = student_repo.get_all_students()
