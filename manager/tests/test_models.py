from sitecustomize import position

from django.contrib.auth import get_user_model
from django.test import TestCase

from manager.models import Position, TaskType, Task


class ModelTest(TestCase):
    def test_str_method_Worker_model(self):
        worker = get_user_model().objects.create(
            username="worker",
            first_name="Tom",
            last_name="Smith",)
        self.assertEqual(str(worker), f"{worker.username}: {worker.first_name} {worker.last_name}")

    def test_str_method_Position_model(self):
        position = Position.objects.create(name="developer")
        self.assertEqual(str(position), position.name)

    def test_str_method_TaskType_model(self):
        task_type = TaskType.objects.create(
            name="Test type")
        self.assertEqual(str(task_type), task_type.name)

    def test_str_method_Task_model(self):
        task_type = TaskType.objects.create(
            name="Test type")
        task = Task.objects.create(
            name="Test task",
            task_type=task_type,
            priority=1,
            deadline="2025-11-11"
        )
        self.assertEqual(str(task), f"Name: {task.name}, type: {task.task_type.name}, priority: {task.priority}")

    def test_create_worker_with_position(self):
        username = "Test_worker"
        password = "Test_password"
        position = Position.objects.create(name="Developer")
        worker = get_user_model().objects.create_user(
            username=username,
            password=password,
            position=position,
        )
        self.assertEqual(worker.username, username)
        self.assertTrue(worker.check_password(password))
        self.assertEqual(worker.position, position)