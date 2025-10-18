from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from .models import Worker, Task

def index(request) -> HttpResponse:
    num_workers = get_user_model().objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context)