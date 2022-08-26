from abc import ABC, ABCMeta, abstractmethod

from fastapi import UploadFile
from pandas import DataFrame


class AbstractExcelService(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def excel_to_dataframe(self, students_file: UploadFile) -> DataFrame:
        raise NotImplementedError

    @abstractmethod
    async def export_list_to_excel(self, excel_file_name, students_list) -> bool:
        raise NotImplementedError
