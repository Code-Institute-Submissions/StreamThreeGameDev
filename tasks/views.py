# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Task
from django.utils import timezone


# Create your views here.
def task_list(request):
    tasks = Task.objects.filter(updated__lte=timezone.now()).order_by('-updated')
    return render(request, "taskmanager.html", {'tasks': tasks})
