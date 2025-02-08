from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Task
from .forms import TaskForm


# Create your views here.

# List all tasks
def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'task_list.html', {'tasks': tasks})

# Add a new task
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

# Edit an existing task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

# Delete a task with confirmation
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})

# Mark a task as complete or incomplete
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')
