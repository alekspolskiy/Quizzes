from django.db import models
from django.utils.translation import gettext_lazy as _
from .common import Base
from .quiz import Quiz
from authentication.models import User


class QuizUser(Base):
    class Meta:
        verbose_name = _('Quiz_User')
        verbose_name_plural = _('Quizes_Users')
        ordering = ['id']

    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
