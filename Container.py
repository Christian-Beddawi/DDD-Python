from dependency_injector import containers, providers
from sqlalchemy import create_engine
from ddd.Application.Service.StudentService import StudentService
from ddd.Domain.RepositoryAbstraction.AbstractStudentRepo import AbstractStudentRepo
from ddd.Domain.ServiceAbstraction.AbstractStudentService import AbstractStudentService
from ddd.Persistence.DBRepo.StudentRepo import StudentRepo
from ddd.Persistence.EngineCreator import EngineCreator


def create_engine_once(config):
    engine = create_engine(config.database.dsn, echo=True)
    # from seedwork.infrastructure.database import Base
    #
    # # TODO: it seems like a hack, but it works...
    # Base.metadata.bind = engine
    return engine


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=["ddd.Presentation.API.endpoints"])

    db_engine = providers.Singleton(EngineCreator, "sqlite:///college.db")

    student_repo = providers.Factory(AbstractStudentRepo.register(StudentRepo), db_engine)

    student_service = providers.Factory(AbstractStudentService.register(StudentService), student_repo)

    # config = providers.Configuration(ini_files=["ddd/Persistence/config.ini"])
    # db = EngineCreator(config)


    # test_service = providers.Factory(TestService, student_helper=student_helper)
    # provider1 = Factory(AbstractStudentHelper)
    # provider2 = Factory(StudentHelper)
    # provider1.override(provider2)
    # some_instance = provider1()
    # assert isinstance(some_instance, StudentHelper)