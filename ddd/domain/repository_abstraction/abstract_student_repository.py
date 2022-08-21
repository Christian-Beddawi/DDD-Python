from abc import ABC, ABCMeta, abstractmethod

from ddd.domain.models.student import Student


class AbstractStudentRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_student(self, student: Student):
        """Add new student to database"""
        raise NotImplementedError

    @abstractmethod
    def add_multiple_students(self, students: dict):
        raise NotImplementedError

    @abstractmethod
    def get_all_students(self):
        raise NotImplementedError
