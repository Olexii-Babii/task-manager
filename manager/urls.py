from django.urls import path

from manager.views import (
    index,
    WorkersListView,
    TasksListView,
    TasksCreateView,
    TaskDetailView,
    TaskDeleteView,
    TaskUpdateView,
    MyTaskListView,
    WorkersDetailView,
    WorkersCreateView,
    WorkersUpdateView,
    WorkersDeleteView,
)

urlpatterns =  [
    path("", index, name="index"),
    path("workers/", WorkersListView.as_view(), name="workers-list"),
    path("tasks/", TasksListView.as_view(), name="tasks-list"),
    path("tasks/create/", TasksCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="tasks-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="tasks-update"),
    path("mytasks/<int:pk>", MyTaskListView.as_view(), name="mytasks-list"),
    path("workers/<int:pk>/", WorkersDetailView.as_view(), name="workers-detail"),
    path("workers/create", WorkersCreateView.as_view(), name="workers-create"),
    path("workers/<int:pk>/update/", WorkersUpdateView.as_view(), name="workers-update"),
    path("workers/<int:pk>/delete/", WorkersDeleteView.as_view(), name="workers-delete"),

]
app_name = "manager"