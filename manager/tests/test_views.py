from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Task, TaskType, Worker, Position

TASK_LIST_URL = reverse("manager:tasks-list")
TASK_DETAIL_URL = reverse("manager:tasks-detail", kwargs={"pk": 1})
WORKER_LIST_URL = reverse("manager:workers-list")
WORKER_DETAIL_URL = reverse("manager:workers-detail", kwargs={"pk": 1})
class PublicTaskTest(TestCase):
    def test_login_required_list_page(self):
        res = self.client.get(TASK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_detail_page(self):
        task_type_2 = TaskType.objects.create(name="QA")
        Task.objects.create(
            name="T1",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        res = self.client.get(TASK_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)


class PublicWorkerTest(TestCase):
    def test_login_required_list_page(self):
        res = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_detail_page(self):
        Worker.objects.create(
            username="test",
            password="test1234",
            position=Position.objects.create(name="developer"))
        res = self.client.get(WORKER_DETAIL_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTaskTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234",
            position=Position.objects.create(name="developer"),
        )
        self.client.force_login(self.user)

    def test_retrieve_list_page(self):
        task_type_2 = TaskType.objects.create(name="QA")
        Task.objects.create(
            name="T1",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        Task.objects.create(
            name="T2",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        res = self.client.get(TASK_LIST_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_detail_page(self):
        task_type_2 = TaskType.objects.create(name="QA")
        Task.objects.create(
            name="T1",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        res = self.client.get(TASK_DETAIL_URL)
        self.assertEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234",
            position=Position.objects.create(name="developer"),
        )
        self.client.force_login(self.user)

    def test_retrieve_list_page(self):
        Worker.objects.create(
            username="test",
            password="test1234",
            position=Position.objects.create(name="QA"))
        Worker.objects.create(
            username="test_user_2",
            password="test1234",
            position=Position.objects.create(name="designer"))
        res = self.client.get(WORKER_LIST_URL)
        self.assertEqual(res.status_code, 200)

    def test_retrieve_detail_page(self):
        Worker.objects.create(
            username="test",
            password="test1234",
            position=Position.objects.create(name="QA"))
        res = self.client.get(WORKER_DETAIL_URL)
        self.assertEqual(res.status_code, 200)