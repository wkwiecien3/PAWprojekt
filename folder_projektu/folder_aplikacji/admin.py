from django.contrib import admin

from .models import Director, Genre, Movie, Series

admin.site.register(Movie),
admin.site.register(Series),
admin.site.register(Genre),
admin.site.register(Director),

