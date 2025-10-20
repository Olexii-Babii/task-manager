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
]
app_name = "manager"