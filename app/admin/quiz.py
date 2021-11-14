from django.contrib import admin
from app import models


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'dt_create', 'name', 'end_date', 'description']
