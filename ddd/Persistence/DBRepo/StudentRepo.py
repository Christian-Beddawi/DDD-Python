from abc import ABCMeta

from sqlalchemy.orm import Session

from ddd.Domain.RepositoryAbstraction.AbstractStudentRepo import AbstractStudentRepo
from ddd.Persistence.Database.Database import Student
from ddd.Persistence.EngineCreator import EngineCreator


class StudentRepo(AbstractStudentRepo):
    __metaclass__ = ABCMeta

    def __init__(self, db_engine_creator: EngineCreator) -> None:
        super().__init__()
        self.db_engine_creator = db_engine_creator

    def add_record(self, student: Student):
        engine = self.db_engine_creator.create_engine_once()
        conn = engine.connect()
        """Add new student to database"""
        ins = Student.insert().values(name=student.first_name, lastname=student.last_name)
        result = conn.execute(ins)
        pass
