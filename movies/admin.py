"""Allows tables to be accessed in admin portal"""
from django.contrib import admin
from .models import Genre, Movie
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    """Adjust the view of genre table"""
    list_display = ("id", "name")

class MovieAdmin(admin.ModelAdmin):
    """Adjust the view of movie table"""
    exclude = ("date_created",)
    list_display = ("title", "release_year", "number_in_stock", "daily_rate")

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
