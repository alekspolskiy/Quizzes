# Generated by Django 2.2.10 on 2021-11-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='anonymously',
            field=models.BooleanField(default=False),
        ),
    ]
