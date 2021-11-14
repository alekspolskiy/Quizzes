from django.db import models
from django.utils.translation import gettext_lazy as _
from .common import Base


class Quiz(Base):
    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizes')
        ordering = ['id']

    name = models.CharField(max_length=63)
    end_date = models.DateTimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
