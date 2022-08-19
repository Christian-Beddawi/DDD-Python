from dependency_injector import containers, providers
from sqlalchemy import create_engine
from ddd.application.service.student_service import StudentService
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepo
from ddd.domain.service_abstraction.abstract_student_service import AbstractStudentService
from ddd.persistence.db_repository.student_repository import StudentRepository
from ddd.persistence.connection_to_db import ConnectionCreator


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["ddd.presentation.api.endpoints"])

    db_engine = providers.Singleton(ConnectionCreator, "sqlite:///college.db")

    student_repo = providers.Factory(AbstractStudentRepo.register(StudentRepository), db_engine)

    student_service = providers.Factory(AbstractStudentService.register(StudentService), student_repo)

    # config = providers.Configuration(ini_files=["ddd/persistence/config.ini"])
    # db = EngineCreator(config)


    # test_service = providers.Factory(TestService, student_helper=student_helper)
    # provider1 = Factory(AbstractStudentHelper)
    # provider2 = Factory(StudentHelper)
    # provider1.override(provider2)
    # some_instance = provider1()
    # assert isinstance(some_instance, StudentHelper)