from django.contrib.auth.models import User, AbstractUser
from django.db import models


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
    assignees = models.ManyToManyField("Worker", related_name="assignees")


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.DO_NOTHING,
        null=True,
    )
