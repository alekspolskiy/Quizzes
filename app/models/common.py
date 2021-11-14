from django.db import models


class Base(models.Model):
    dt_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
