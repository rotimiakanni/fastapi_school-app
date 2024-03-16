from pydantic import BaseModel
from ..schemas.students import Student

class Level(BaseModel):
    name: str
    students: list[Student]