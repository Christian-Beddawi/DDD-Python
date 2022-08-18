from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Student(BaseModel):
    id: Optional[int] = None,
    first_name: str
    last_name: str
    DOB: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Christian",
                "last_name": "Beddawi",
                "DOB": "2001-18-01 08:30:54"
            }
        }