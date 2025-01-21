from django.contrib import admin

from .models import Director, Genre, Movie, Series, Studio

admin.site.register(Movie),
admin.site.register(Series),
admin.site.register(Genre),
admin.site.register(Director),
admin.site.register(Studio)
