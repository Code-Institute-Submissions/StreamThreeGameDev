from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    # ?P<id>\d+) means that django will take the value passed and
    # transfer to a view as a variable called id
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post, name='edit'),
]