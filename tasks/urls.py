from django.conf.urls import url
import views

urlpatterns = [
    url(r'^tasks/', views.task_list, name='task_list'),
    url(r'^new_task/', views.new_task, name='new_task'),
    url(r'^(?P<id>\d+)/edit_task$', views.edit_task, name='edit_task'),
]
