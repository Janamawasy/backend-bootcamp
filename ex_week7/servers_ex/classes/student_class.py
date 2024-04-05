from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    name: str
    id: str
    age: int
    classes: List[str]