"""This is to keep a list of movie paths"""
# pylint: disable = no-member
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home")
]
