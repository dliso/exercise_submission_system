from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exercise/([0-9]+)/$', views.exercise, name='exercise'),
    url(r'^exercise/([0-9]+)/handin/$', views.hand_in_exercise, name='hand_in_exercise'),
    url(r'^exercise/add/$', views.add_exercise, name='add_exercise'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
]
