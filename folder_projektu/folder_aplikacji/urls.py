from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('series/', views.series_list),
    path('series/<int:pk>/', views.series_detail),
    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_detail),
    path('director/', views.director_list),
    path('director/<int:pk>/', views.director_detail),
    path('studio/', views.studio_list),
    path('studio/<int:pk>/', views.studio_detail),
    path('director/', views.director_list),
    path('director/<int:pk>/', views.director_detail),
]