from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from manager.models import Worker, Task, TaskType, Position


class SearchTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="Testuser",
            password="test1234"
        )
        self.client.force_login(self.user)

    def test_task_correct_search(self):
        task_type_1 = TaskType.objects.create(name="Refactor")
        task_type_2 = TaskType.objects.create(name="QA")

        task_1 = Task.objects.create(
            name="T1",
            deadline="2025-11-11",
            task_type=task_type_1,
        )
        task_2 = Task.objects.create(
            name="Q2",
            deadline="2025-11-11",
            task_type=task_type_1,
        )
        task_3 = Task.objects.create(
            name="R3",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        task_4 = Task.objects.create(
            name="F1",
            deadline="2025-11-11",
            task_type=task_type_2,
        )
        url = reverse("manager:tasks-list")
        res = self.client.get(f"{url}?parameter=r")
        self.assertEqual(list(res.context["task_list"]), [task_1, task_2, task_3])

        new_url_1 = reverse("manager:tasks-list")
        new_res_1 = self.client.get(new_url_1)
        self.assertEqual(
            list(new_res_1.context["task_list"]),
            list(Task.objects.all()))

        new_url_2 = reverse("manager:tasks-list")
        new_res_2 = self.client.get(f"{new_url_2}?parameter=x")
        self.assertEqual(list(new_res_2.context["task_list"]), [])



    def test_worker_correct_search(self):
        position_1 = Position.objects.create(name="developer")
        position_2 = Position.objects.create(name="manager")
        worker_1 = get_user_model().objects.create_user(
            username="designer",
            first_name="John",
            last_name="Doe",
            password="testuser1",
            position=position_2,
        )
        worker_2 = get_user_model().objects.create_user(
            username="superman",
            first_name="Tom",
            last_name="Smith",
            password="testuser2",
            position=position_1,
        )
        get_user_model().objects.create_user(
            username="batman",
            first_name="Jeremmy",
            last_name="Born",
            password="testuser3",
            position=position_2,
        )
        worker_3 = get_user_model().objects.create_user(
            username="iron_wolf",
            first_name="Bob",
            last_name="Biden",
            password="testuser3",
            position=position_2,
        )
        url = reverse("manager:workers-list")
        res = self.client.get(f"{url}?parameter=de")
        self.assertEqual(
            list(res.context["worker_list"]),
            [worker_1, worker_2, worker_3]
        )

        new_url_1 = reverse("manager:workers-list")
        new_res = self.client.get(new_url_1)
        self.assertEqual(
            list(new_res.context["worker_list"]),
            list(get_user_model().objects.all()))

        new_url_2 = reverse("manager:workers-list")
        new_res_2 = self.client.get(f"{new_url_2}?parameter=xy")
        self.assertEqual(list(new_res_2.context["worker_list"]), [])
