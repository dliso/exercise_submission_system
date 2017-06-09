from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exercise/([0-9]+)/$', views.exercise, name='exercise'),
]
