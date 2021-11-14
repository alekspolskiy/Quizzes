from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _
from .quiz import Quiz
from .common import Base
from app import enums


class Question(Base):
    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ['id']

    text = models.CharField(max_length=255)
    type = models.CharField(max_length=63, choices=enums.QuestionType.choices())
    answer_options = JSONField(null=True)
    quiz = models.ForeignKey(Quiz, related_name='question', on_delete=models.DO_NOTHING)

