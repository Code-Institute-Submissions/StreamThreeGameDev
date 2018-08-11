# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = (
        ('Todo', 'Todo'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    )

    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200, null=False)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    description = models.CharField(max_length=255, null=False)
    updated = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title
