from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.timezone import now
from apps.todo.manager import TaskManager


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField('Title', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Priority = [('A', 'A'), ('B', 'B'), ('C', 'C')]
    priority = models.CharField('Priority', max_length=1, choices=Priority)
    content = models.TextField('Content', blank=True)
    time_to_do = models.DateTimeField('Time to do', help_text='format :2021-05-22 15:30')
    created = models.DateTimeField(default=now)
    done = models.BooleanField(default=False)

    objects = TaskManager()

    class Meta:
        ordering = ["time_to_do"]

    def __str__(self):
        return self.title + " " + self.priority

    def get_absolute_url(self):
        try:
            return reverse('task_detail', args=(str(self.id)))
        except NoReverseMatch:
            return reverse('404')
