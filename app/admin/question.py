from django.contrib import admin
from app import models
from .answer import AnswerInlineModel


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'quiz']
    list_display = ['id', 'dt_create', 'text', 'quiz']
    inlines = [AnswerInlineModel]
