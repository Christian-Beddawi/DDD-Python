from datetime import datetime
from pydantic import BaseModel


class GetStudentsResponseModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: datetime
