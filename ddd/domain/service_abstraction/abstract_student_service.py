from abc import ABC, ABCMeta, abstractmethod

from ddd.domain.models.student import Student


class AbstractStudentService(ABC):
    __metaclass__ = ABCMeta

    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     return (hasattr(subclass, 'insert_student') and
    #             callable(subclass.insert_student) and
    #             hasattr(subclass, 'extract_text') and
    #             callable(subclass.extract_text))

    @abstractmethod
    def insert_student(self, student: Student):
        """Add new student to database"""
        raise NotImplementedError
