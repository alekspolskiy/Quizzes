from pydantic import BaseModel
from typing import Any


class QuizUserCreateUpdate(BaseModel):
    quiz: Any
    user: Any
