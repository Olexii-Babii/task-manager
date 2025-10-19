from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Worker, Task

def index(request) -> HttpResponse:
    num_workers = get_user_model().objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context)


class WorkersListView(generic.ListView):
    model = Worker
    paginate_by = 10
    queryset = Worker.objects.all().select_related("position")


class TasksListView(generic.ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.select_related("task_type")
