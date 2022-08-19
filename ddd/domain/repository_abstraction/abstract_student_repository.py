from abc import ABC, ABCMeta, abstractmethod


from ddd.domain.models.student import Student


class AbstractStudentRepository(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_student(self, student: Student):
        """Add new student to database"""
        raise NotImplementedError

    @abstractmethod
    def get_all_students(self):
       raise NotImplementedError