from pydantic import BaseModel
from typing import Optional, Any


class TypingOrChooseOneAnswerCreate(BaseModel):
    text: Any
    username: Optional[str]
    anonymously: bool
    question: Any
    user: Any


class AnswerResponseAPI(BaseModel):
    text: Any
    username: Any
    anonymously: bool

    class Config:
        orm_mode = True
