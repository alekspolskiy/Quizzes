from typing import Any


class Constants:
    """
    A base class for defining a class with a set of constants.
    Implements property "all" to get all values of constants.
    The child class attributes must be set in upper case.
    """
    value_type: Any

    @classmethod
    def all(cls) -> tuple:
        keys = [
            key
            for key, value in cls.__dict__.items()
            if isinstance(value, cls.value_type) and key.isupper()
        ]
        return tuple([getattr(cls, key) for key in keys])

    @classmethod
    def list(cls, name, value, underscore_replacement=" ") -> list:
        """
        Convert to list with dict
        :param name: key for «human read value»
        :param value: key for value
        :param underscore_replacement: replacement for underscore
        :return:
        """
        return [{name: k.replace("_", underscore_replacement).capitalize(), value: k} for k in cls.all()]

    @classmethod
    def to_order(cls, value):
        statuses = cls.all()
        try:
            return statuses.index(value)
        except ValueError:
            return 0

    @classmethod
    def labels(cls, *args, **kwargs):
        return {}

    @classmethod
    def label(cls, value, *args, **kwargs):
        return cls.labels(*args, **kwargs)[value] if value in cls.labels().keys() else None


class StrConstants(Constants):
    """
    A base class for defining a class with a set of string constants.

    Examples
    --------
    >>> class ExampleClass(object, metaclass=StrConstants):
    ...     FIRST = 'first'
    ...     SECOND = 'second'
    ...     THIRD = 'third'
    ...
    >>> print(ExampleClass.all())
    ... ('first', 'second', 'third')
    """
    value_type = str


class QuestionType(StrConstants):
    """
    A class for question type:
    typing - answer in text
    choose_one - answer with only one given variant
    choose_many - answer with a few given variants
    """
    TYPING = "typing"
    CHOOSE_ONE = "choose_one"
    CHOOSE_MANY = "choose_many"


class APIErrorCode(StrConstants):
    """
    A class that contains constants for errors that the API returns.
    """
    INVALID_DATA = "INVALID_DATA"
    ENTITY_NOT_FOUND = "ENTITY_NOT_FOUND"
    ANSWERED = "YOU ALREADY ANSWERED THIS QUESTION"
    WRONG_ONE_ANSWER = "WRONG ANSWER. PLEASE CHOOSE ONE CORRECT ANSWER"
    WRONG_COUNT_ANSWERS = "WRONG ANSWER. PLEASE CHOOSE A MORE THEN ONE ANSWER"
    WRONG_MANY_ANSWERS = "WRONG ANSWERS. PLEASE CHOOSE A CORRECT ANSWERS"
    WRONG_DATA_TYPE = "ANSWER MUST BE STRING"
