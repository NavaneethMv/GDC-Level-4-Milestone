from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render



tasks = []
completed = []

def task_view(request):
    return render(request, "tasks.html", {"tasks": tasks})

def add_task_view(request):
    task = request.GET.get("task")
    tasks.append(task)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
    tasks.pop(index-1)
    return HttpResponseRedirect("/tasks")

def complete_task_view(request, index):
    completed_task = tasks.pop(index-1)
    completed.append(completed_task)
    return HttpResponseRedirect("/tasks")

def completed_task_view(request):
    return render(request, "completed.html", {"completed": completed})
    
def all_tasks_view(request):
    return render(request, "all_tasks.html", {"tasks": tasks, "completed": completed})