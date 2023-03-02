"""This is for setting up the tables for the database"""
from django.db import models

class Genre(models.Model):
    """This is the Genre table"""
    name = models.CharField(max_length=255)


class Movie(models.Model):
    """
        This is the Movie Table
        Has-One Genre
    """
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
