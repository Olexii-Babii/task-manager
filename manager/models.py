from django.contrib.auth.models import User, AbstractUser
from django.db import models

from task_manager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    class StrChoices(models.TextChoices):
        URGENT = "URG", "Urgent"
        HIGH = "HI", "High"
        MEDIUM = "MED", "Medium"
        LOW = "LOW", "Low"

    name = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=3,
        choices=StrChoices.choices,
        default=StrChoices.MEDIUM,
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="assignees")

    def __str__(self):
        return f"Name: {self.name}, type: {self.task_type.name}, priority: {self.priority}"

class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.DO_NOTHING,
        null=True,
    )

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
