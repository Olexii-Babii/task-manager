from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import WorkerCreationForm, WorkerUpdateForm, TaskForm, TaskSearchForm, WorkerSearchForm
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

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super(WorkersListView, self).get_context_data(**kwargs)
        context["search_form"] = WorkerSearchForm()
        return context

    def get_queryset(self):
        param = self.request.GET.get("parameter")
        if param:
            return self.queryset.filter(
                Q(username__icontains=param) |
                Q(first_name__icontains=param) |
                Q(last_name__icontains=param) |
                Q(position__name__icontains=param))
        return self.queryset.all()


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    queryset = Task.objects.select_related("task_type")

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()
        return context

    def get_queryset(self):
        param = self.request.GET.get("parameter")
        if param:
            return self.queryset.filter(
                Q(name__icontains=param) |
                Q(task_type__name__icontains=param))
        return self.queryset.all()


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TasksCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:tasks-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:tasks-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:tasks-list")


class MyTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 10
    template_name = "manager/task_list.html"

    def get_context_data(
            self, *, object_list=..., **kwargs
    ):
        context = super(MyTaskListView, self).get_context_data(**kwargs)
        context["search_form"] = TaskSearchForm()
        return context

    def get_queryset(self):
        queryset =  Task.objects.filter(id=self.kwargs["pk"]).select_related("task_type")
        param = self.request.GET.get("parameter")
        if param:
            return queryset.filter(
                Q(name__icontains=param) |
                Q(task_type__name__icontains=param))
        return queryset.all()




class WorkersDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("manager:workers-list")


class WorkersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("manager:workers-list")


class WorkersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:workers-list")