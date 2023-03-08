"""This is to keep a list of movie paths"""
# pylint: disable = no-member, invalid-name
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>", views.detail, name="detail")
]
