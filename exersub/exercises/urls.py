from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exercise/([0-9]+)/$', views.exercise, name='exercise'),
    url(r'^exercise/add/$', views.add_exercise, name='add_exercise'),
    url(r'^groups/([0-9]+)/$', views.group, name='group'),
    url(r'^groups/create/$', views.create_group, name='create_group'),
]
