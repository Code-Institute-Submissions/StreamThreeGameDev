# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone
from .forms import TaskForm


# Create your views here.
def task_list(request):
    tasks = Task.objects.filter(updated__lte=timezone.now()).order_by('-updated')
    return render(request, "taskmanager.html", {'tasks': tasks})


def new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.updated = timezone.now()
            task.save()
            return redirect(task_list)
    else:
        form = TaskForm()
    return render(request, "taskform.html", {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.updated = timezone.now()
            task.save()
            return redirect(task_list)
    else:
        form = TaskForm(instance=task)
    return render(request, "taskform.html", {'form': form})
