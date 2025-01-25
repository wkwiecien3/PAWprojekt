from django.contrib import admin
from .models import Director, Genre, Movie, Series, Studio

class StudioAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_of_establishment', 'location']
    list_filter = ['name']

admin.site.register(Studio, StudioAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'studio', 'rating']
    list_filter = ['genre']

admin.site.register(Movie, MovieAdmin)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'studio', 'episodes_watched', 'rating']
    list_filter = ['genre']

admin.site.register(Series, SeriesAdmin),
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id']

admin.site.register(Genre, GenreAdmin),
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'year_born']
    list_filter = ['name']

admin.site.register(Director, DirectorAdmin),


