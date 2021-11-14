from enum import Enum
from factoryproject import constants


class QuestionType(Enum):
    """Enums for questions"""
    TYPING = constants.QuestionType.TYPING
    CHOOSE_ONE = constants.QuestionType.CHOOSE_ONE
    CHOOSE_MANY = constants.QuestionType.CHOOSE_MANY

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
