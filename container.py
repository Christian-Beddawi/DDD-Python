from dependency_injector import containers, providers
from ddd.Infrastructure.authentication.authentication import Authentication
from ddd.Infrastructure.external_api.external_api_repository import ExternalApiRepository
from ddd.application.authentication.login_service import LoginWithGoogleFirebase
from ddd.application.authentication.refresh_token_service import RefreshJwtToken
from ddd.application.external_api_service.get_university_from_external_api import GetUniversityFormExternalApi
from ddd.application.student.commands.insert_student.insert_student_command import InsertStudentCommand
from ddd.application.student.commands.insert_students_from_excel.insert_students_from_excel_file_command import InsertStudentsFromExcelCommand
from ddd.application.student.queries.get_students_by_name.get_students_by_name_query import GetStudentsByNameQuery
from ddd.application.student.queries.get_students_excel_file.get_students_excel_file_query import GetStudentsExcelQuery
from ddd.application.student.queries.get_students.get_students_query import GetStudentsQuery
from ddd.domain.authentication_abstraction.abstract_authentication import AuthenticationAbstraction
from ddd.domain.excel_service_abstraction.abstract_excel_service import AbstractExcelService
from ddd.domain.external_api_abstraction.abstract_get_university_from_external_api import \
    AbstractGetUniversityFormExternalApi
from ddd.domain.external_api_abstraction.external_api_repository_abstraction import AbstractExternalApiRepository
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from ddd.persistence.db_repository.student_repository import StudentRepository
from ddd.persistence.database.connection_to_db import ConnectionCreator
from ddd.shared.excel_related_services.excel_service import ExcelService


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["ddd.presentation.api.students_controller"])

    # db_engine = providers.Singleton(ConnectionCreator, "sqlite:///college.db") # SQLAlchemy
    # db_connection = providers.Singleton(ConnectionCreator, "mongodb://localhost/ums") # MongoEngine
    db = providers.Singleton(ConnectionCreator, "mongodb://localhost/", "ums")  # MongoEngine

    student_repo = providers.Factory(AbstractStudentRepository.register(StudentRepository), db)

    authentication = providers.Singleton(AuthenticationAbstraction.register(Authentication))

    login_with_firebase = providers.Factory(LoginWithGoogleFirebase, authentication=authentication)

    refresh_jwt_token = providers.Factory(RefreshJwtToken, authentication=authentication)

    excel_service = providers.Factory(AbstractExcelService.register(ExcelService))

    get_students_excel_query = providers.Factory(GetStudentsExcelQuery, student_repo=student_repo, excel_service=excel_service)

    get_students_query = providers.Factory(GetStudentsQuery, student_repo=student_repo)

    get_students_by_name_query = providers.Factory(GetStudentsByNameQuery, student_repo=student_repo)

    insert_student_command = providers.Factory(InsertStudentCommand, student_repo=student_repo)

    insert_students_from_excel_command = providers.Factory(InsertStudentsFromExcelCommand, student_repo=student_repo, excel_service=excel_service)

    external_api_repository = providers.Factory(AbstractExternalApiRepository.register(ExternalApiRepository), "http://127.0.0.1:5000/university")

    abstract_get_uni_from_external_api = providers.Factory(AbstractGetUniversityFormExternalApi.register(GetUniversityFormExternalApi), external_api_repository)


    # student_service = providers.Factory(AbstractStudentService.register(StudentService), student_repo)

    # config = providers.Configuration(ini_files=["ddd/persistence/config.ini"])
    # db = EngineCreator(config)


    # test_service = providers.Factory(TestService, student_helper=student_helper)
    # provider1 = Factory(AbstractStudentHelper)
    # provider2 = Factory(StudentHelper)
    # provider1.override(provider2)
    # some_instance = provider1()
    # assert isinstance(some_instance, StudentHelper)