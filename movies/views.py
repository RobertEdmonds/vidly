"""This is for restful routes of movie"""
# pylint: disable = no-name-in-module
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    """This is to send movies to http"""
    movies = Movie.objects.all()
    return render(request, "index.html", {"movies": movies})

def home(request):
    """To add value to home page"""
    return HttpResponse("Hello")
