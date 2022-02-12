from django.contrib import admin
from django.urls import path, re_path
import tasks.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index_view),
    path("tasks/", views.task_view),
    path("add-task/", views.add_task_view),
    path("delete-task/<int:index>/", views.delete_task_view),
    path("complete_task/<int:index>/", views.complete_task_view),
    path("completed_tasks/", views.completed_task_view),
    path("all_tasks/", views.all_tasks_view)
]
