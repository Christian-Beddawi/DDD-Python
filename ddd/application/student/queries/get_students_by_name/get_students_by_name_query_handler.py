from typing import List

from mediatr import Mediator

from ddd.application.student.queries.get_students.get_students_query import GetStudentsQuery
from ddd.application.student.queries.get_students.get_students_response_model import GetStudentsResponseModel
from ddd.application.student.queries.get_students_by_name.get_students_by_name_query import GetStudentsByNameQuery
from ddd.domain.exceptions.not_found_exception import NotFoundException


@Mediator.handler
class GetStudentsByNameQueryHandler:
    def handle(self, request: GetStudentsByNameQuery) -> List[GetStudentsResponseModel]:
        try:
            return request.student_repo.get_students_by_name(request.name)
        except NotFoundException as ex:
            raise ex
