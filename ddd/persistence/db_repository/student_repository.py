# from abc import ABCMeta
# import sqlalchemy as db
from typing import List
from ddd.domain.exceptions.not_found_exception import NotFoundException
from ddd.domain.models.student import Student
from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
# from ddd.persistence.database.database import Students
from ddd.persistence.database.connection_to_db import ConnectionCreator
# from ddd.persistence.database.database import Student as Stud


class StudentRepository(AbstractStudentRepository):

    def __init__(self, db_connection_creator: ConnectionCreator) -> None:
        self.db_connection_creator = db_connection_creator
        self.db = self.db_connection_creator.db  # PyMongo

    def add_student(self, student: Student):
        # PyMongo
        self.db['students'].insert_one(student.dict())
        # MongoEngine
        """s = Students(first_name=student.first_name, last_name=student.last_name, dob=student.dob)
        s.save()"""

    def add_multiple_students(self, students: dict):
        self.db['students'].insert_many(students)  # PyMongo

    def get_all_students(self) -> List[Student]:
        # PyMongo
        students_cursor = self.db['students'].find()
        students = list(students_cursor)
        for num, stud in enumerate(students):
            # convert ObjectId() to str
            stud["_id"] = str(stud["_id"])
        return students
        # MongoEngine
        """students = []
        for student in Students.objects:
            students.append([student.first_name, student.last_name, student.dob if student.dob!=None else "Unknown"])
        return students"""
        # SQLAlchemy
        "return self.db_connection_creator.conn.execute(db.select([Stud])).fetchall()"

    def get_students_by_name(self, name: str) -> List[Student]:
        students_cursor = self.db['students'].find({"first_name": name})
        students = list(students_cursor)
        for num, stud in enumerate(students):
            # convert ObjectId() to str
            stud["_id"] = str(stud["_id"])
        if len(students) == 0:
            raise NotFoundException()
        return students
