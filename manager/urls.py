from django.urls import path

from manager.views import index, WorkersListView, TasksListView

urlpatterns =  [
    path("", index, name="index"),
    path("workers/", WorkersListView.as_view(), name="workers-list"),
    path("tasks/", TasksListView.as_view(), name="tasks-list"),
]
app_name = "manager"