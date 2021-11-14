from django.contrib import admin
from app import models


@admin.register(models.QuizUser)
class QuizUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'quiz_id', 'user_id']
