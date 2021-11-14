from .base import BaseCRUD
from app import models
from app import schemas


class QuizUserCRUD(
    BaseCRUD[
        schemas.QuizUserCreateUpdate,
        schemas.QuizUserCreateUpdate,
    ]
):
    pass


quiz_user = QuizUserCRUD(model=models.QuizUser)
