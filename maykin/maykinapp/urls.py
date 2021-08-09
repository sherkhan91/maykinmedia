from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('startcornjob', views.startcornjob, name='startcornjob'),
]