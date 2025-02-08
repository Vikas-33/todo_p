from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Show all tasks
    path('add/', views.add_task, name='add_task'),  # Add new task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit a task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete a task
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),  # Mark task complete/incomplete
]
