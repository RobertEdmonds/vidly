"""This is for restful routes of movie"""
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    """This is to send movies to http"""
    movies = Movie.objects.all()
    output = ", ".join([m.title for m in movies])
    return HttpResponse(output)
