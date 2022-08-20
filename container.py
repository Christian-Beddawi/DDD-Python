from dependency_injector import containers, providers

from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from ddd.persistence.db_repository.student_repository import StudentRepository
from ddd.persistence.database.connection_to_db import ConnectionCreator


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["ddd.presentation.api.endpoints"])

    # db_engine = providers.Singleton(ConnectionCreator, "sqlite:///college.db")
    db_connection = providers.Singleton(ConnectionCreator, "mongodb://localhost/ums")

    student_repo = providers.Factory(AbstractStudentRepository.register(StudentRepository), db_connection)

    #Removed after using cqrs
    # student_service = providers.Factory(AbstractStudentService.register(StudentService), student_repo)

    # config = providers.Configuration(ini_files=["ddd/persistence/config.ini"])
    # db = EngineCreator(config)


    # test_service = providers.Factory(TestService, student_helper=student_helper)
    # provider1 = Factory(AbstractStudentHelper)
    # provider2 = Factory(StudentHelper)
    # provider1.override(provider2)
    # some_instance = provider1()
    # assert isinstance(some_instance, StudentHelper)