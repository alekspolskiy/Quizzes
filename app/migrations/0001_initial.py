# Generated by Django 2.2.10 on 2021-11-13 22:24

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=63)),
                ('end_date', models.DateTimeField()),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('TYPING', 'typing'), ('CHOOSE_ONE', 'choose_one'), ('CHOOSE_MANY', 'choose_many')], max_length=63)),
                ('answer_options', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='app.Quiz')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_create', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answer', to='app.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'ordering': ['id'],
            },
        ),
    ]
