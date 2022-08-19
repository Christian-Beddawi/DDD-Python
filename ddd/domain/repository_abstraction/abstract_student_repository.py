from abc import ABC, ABCMeta, abstractmethod


from ddd.domain.models.student import Student


class AbstractStudentRepo(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_record(self, student: Student):
        """Add new student to database"""
        raise NotImplementedError
