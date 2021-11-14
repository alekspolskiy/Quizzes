from django.db import models
from django.utils.translation import gettext_lazy as _
from .question import Question
from authentication.models import User
from .common import Base


class Answer(Base):
    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ['id']

    text = models.CharField(max_length=255)
    anonymously = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=True)
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
