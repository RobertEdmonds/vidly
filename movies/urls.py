"""This is to keep a list of movie paths"""
# pylint: disable = no-member
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="movies_index"),
    path("<int:movie_id>", views.detail, name="movies_detail")
]
