from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InsertStudentCommandModel(BaseModel):
    first_name: str
    last_name: str
    dob: Optional[datetime] = None
