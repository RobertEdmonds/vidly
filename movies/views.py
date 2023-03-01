from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    """This is to send movies to http"""
    return HttpResponse("Hello World")
