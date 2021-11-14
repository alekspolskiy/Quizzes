from pydantic import BaseModel, root_validator
from typing import Optional, Any
from app import enums


class QuestionCreate(BaseModel):
    text: str
    type: enums.QuestionType
    answer_options: Optional[dict]
    quiz: Any

    @root_validator()
    def validate_root(cls, values):
        values["type"] = values.get("type").value
        return values


class QuestionUpdate(BaseModel):
    text: Optional[str]
    type: Optional[enums.QuestionType]
    answer_options: Optional[dict]

    @root_validator()
    def validate_root(cls, values):
        values["type"] = values.get("type").value if values["type"] else None
        return values


class QuestionResponseAPI(BaseModel):
    text: str
    type: str
    answer_options: Optional[Any]
    quiz_id: int

    class Config:
        orm_mode = True


class QuestionWithAnswerResponseAPI(BaseModel):
    question_num: int
    text: str
    type: str
    answer_options: Optional[Any]
    answer: Any

    class Config:
        orm_mode = True
