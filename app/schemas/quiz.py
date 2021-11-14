from pydantic import BaseModel
from typing import Any


class QuizCreateUpdate(BaseModel):
    name: str
    end_date: Any
    description: str

    class Config:
        orm_mode = True


class QuizesResponseAPI(BaseModel):
    name: str
    end_date: Any
    description: str
    questions: list

    class Config:
        orm_mode = True
