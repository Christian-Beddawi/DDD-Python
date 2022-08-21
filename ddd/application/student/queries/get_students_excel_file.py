from ddd.domain.repository_abstraction.abstract_student_repository import AbstractStudentRepository
import pandas as pd


class GetStudentsExcel:
    def __init__(self, excel_file_name, student_repo: AbstractStudentRepository):
        self.student_repo = student_repo
        students_list = student_repo.get_all_students()
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
