from abc import ABCMeta

from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepo
from ddd.persistence.database.database import Student
from ddd.persistence.connection_to_db import ConnectionCreator


class StudentRepository(AbstractStudentRepo):
    __metaclass__ = ABCMeta

    def __init__(self, db_engine_creator: ConnectionCreator) -> None:
        self.db_engine_creator = db_engine_creator

    def add_record(self, student: Student):
        """Add new student to database"""
        conn = self.db_engine_creator.conn
        ins = Student.insert().values(name=student.first_name, lastname=student.last_name)
        conn.execute(ins)
