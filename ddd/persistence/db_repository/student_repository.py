from abc import ABCMeta
import sqlalchemy as db

from ddd.domain.models.student import Student
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
from ddd.persistence.database.database import Students
from ddd.persistence.database.connection_to_db import ConnectionCreator
# from ddd.persistence.database.database import Student as Stud


class StudentRepository(AbstractStudentRepository):
    __metaclass__ = ABCMeta

    def __init__(self, db_connection_creator: ConnectionCreator) -> None:
        self.db_connection_creator = db_connection_creator

    def add_student(self, student: Student):
        """Add new student to database"""
        s = Students(first_name=student.first_name, last_name=student.last_name, dob=student.dob)
        s.save()

    def get_all_students(self):
        students = []
        for student in Students.objects:
            students.append([student.first_name, student.last_name, student.dob if student.dob!=None else "Unknown"])
        return students
        # return self.db_connection_creator.conn.execute(db.select([Stud])).fetchall()
