"""This is for restful routes of movie"""
# pylint: disable = no-name-in-module
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    """This is to send movies to http"""
    movies = Movie.objects.all()
    return render(request, "movies/index.html", {"movies": movies})

def detail(request, movie_id):
    """To add value to home page"""
    movie = Movie.objects.get(pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
