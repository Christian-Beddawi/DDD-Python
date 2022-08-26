import pandas as pd
from fastapi import UploadFile
from pandas import DataFrame
from ddd.domain.excel_service_abstraction.abstract_excel_service import AbstractExcelService


class ExcelService(AbstractExcelService):

    def excel_to_dataframe(self, students_file: UploadFile) -> DataFrame:
        return pd.read_excel(students_file.filename)

    def export_list_to_excel(self, excel_file_name, students_list) -> bool:
        try:
            students_df = pd.DataFrame(columns=[])
            for num, doc in enumerate(students_list):
                # get document _id from dict
                doc_id = doc["_id"]
                # create a Series obj from the MongoDB dict
                series_obj = pd.Series(doc, name=doc_id)
                # append the MongoDB Series obj to the DataFrame obj
                students_df = students_df.append(series_obj)

            with pd.ExcelWriter(excel_file_name + '.xlsx') as writer:
                students_df.to_excel(writer)
            return True
        except:
            return False
