from django.contrib.auth.models import AbstractUser
from django.db import models

from task_manager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class StrChoices(models.TextChoices):
        URGENT = "1", "Urgent"
        HIGH = "2", "High"
        MEDIUM = "3", "Medium"
        LOW = "4", "Low"

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
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "priority"]

    def __str__(self):
        return f"Name: {self.name}, type: {self.task_type.name}, priority: {self.priority}"

class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.DO_NOTHING,
        null=True,
    )
    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
