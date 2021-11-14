from django.contrib import admin
from app import models


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question']


class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = ['text', ]
