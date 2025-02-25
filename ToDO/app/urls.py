from django.urls import path
from .views import homePage, add_task, delete_task, update_task

urlpatterns = [
    path("", homePage, name="home"),
    path("add-task/", add_task, name="add_task"),
    path("delete-task/<int:task_id>/", delete_task, name="delete_task"),
    path("update-task/<int:task_id>/", update_task, name="update_task"),
]
