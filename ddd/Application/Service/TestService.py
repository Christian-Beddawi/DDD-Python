from ddd.Domain.ServiceAbstraction.AbstractStudentService import AbstractStudentService


class TestService():
    def __init__(self, student_service: AbstractStudentService):
        self.student_service = student_service

    # def shi(self):
    #     self.student_service.
