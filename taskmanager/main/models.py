from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    event_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
