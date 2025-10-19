from django.urls import path

from manager.views import index, WorkersListView

urlpatterns =  [
    path("", index, name="index"),
    path("workers/", WorkersListView.as_view(), name="workers-list"),
]
app_name = "manager"