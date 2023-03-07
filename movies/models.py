"""This is for setting up the tables for the database"""
from django.db import models
from django.utils import timezone

class Genre(models.Model):
    """This is the Genre for movies table"""
    name = str(models.CharField(max_length=255))

    def __str__(self):
        return self.name


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
    date_created = models.DateTimeField(default=timezone.now)
