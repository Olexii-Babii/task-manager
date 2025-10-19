from django.urls import path

from manager.views import index, WorkersListView, TasksListView, TasksCreateView, TaskDetailView

urlpatterns =  [
    path("", index, name="index"),
    path("workers/", WorkersListView.as_view(), name="workers-list"),
    path("tasks/", TasksListView.as_view(), name="tasks-list"),
    path("tasks/create/", TasksCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
]
app_name = "manager"