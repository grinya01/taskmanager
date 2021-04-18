# Generated by Django 3.1.4 on 2021-03-04 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_task_tretret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tretret',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.CharField(default=1, max_length=10, verbose_name='Дата добавления заметки'),
            preserve_default=False,
        ),
    ]
