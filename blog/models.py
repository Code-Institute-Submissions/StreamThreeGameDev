# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """
    Defining the Post model with the attributes a
    post will have:
    Author, Title, Content, Created date and Published date
    """

    # the author is linked to a registered user,
    # using the user model in the auth app
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    # when the blog entry is published, this function will
    # be called to update the database
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
