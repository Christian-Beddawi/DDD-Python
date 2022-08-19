from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Student(BaseModel):
    id: Optional[int] = None,
    first_name: str
    last_name: str
    DOB: Optional[datetime] = None
