"""This is to keep a list of movie paths"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
]
