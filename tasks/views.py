from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('tasks_list')
    return render(request, 'tasks/tasks_form.html', {'form': form, 'title': 'Edit Task'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')
    return render(request, 'tasks/tasks_confirm_delete.html', {'task': task})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return redirect('tasks_list')
    return render(request, 'tasks/tasks_form.html', {'form': form, 'title': 'Create Task'})