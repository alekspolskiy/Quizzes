from django.contrib import admin
from authentication import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'last_login',  'username', 'email']
