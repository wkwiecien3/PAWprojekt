from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.Movie_list),
    path('movies/<int:pk>/', views.Movie_detail),
    path('series/', views.Series_list),
    path('series/<int:pk>/', views.Series_detail),
]