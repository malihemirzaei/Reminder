from django.db import models
from django.utils.timezone import now


class TaskManager(models.Manager):
    def past_tasks(self):
        return super().get_queryset().filter(time_to_do__lt=now(), done=False)

