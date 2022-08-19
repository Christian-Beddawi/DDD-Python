from abc import ABCMeta
import sqlalchemy as db
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from ddd.persistence.database.database import Student
from ddd.persistence.connection_to_db import ConnectionCreator
from ddd.persistence.database.database import Student as Stud


class StudentRepository(AbstractStudentRepository):
    __metaclass__ = ABCMeta

    def __init__(self, db_engine_creator: ConnectionCreator) -> None:
        self.db_engine_creator = db_engine_creator

    def add_student(self, student: Student):
        """Add new student to database"""
        conn = self.db_engine_creator.conn
        ins = Student.insert().values(name=student.first_name, lastname=student.last_name)
        conn.execute(ins)

    def get_all_students(self):
        """Add new student to database"""
        return self.db_engine_creator.conn.execute(db.select([Stud])).fetchall()
