from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

# from .forms import TaskForm
from .models import Worker, Task

def index(request) -> HttpResponse:
    num_workers = get_user_model().objects.count()
    num_tasks = Task.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
    }
    return render(request, "manager/index.html", context)


class WorkersListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10
    queryset = Worker.objects.all().select_related("position")


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.select_related("task_type")

class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TasksCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:tasks-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:tasks-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("manager:tasks-list")