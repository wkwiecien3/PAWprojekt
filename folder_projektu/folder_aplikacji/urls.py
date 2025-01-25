from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('movies/update/<int:pk>/', views.movie_update),
    path('movies/delete/<int:pk>/', views.movie_delete),
    path('series/', views.series_list),
    path('series/<int:pk>/', views.series_detail),
    path('series/search/<str:substring>/', views.series_search),
    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_detail),
    path('director/', views.director_list),
    path('director/<int:pk>/', views.director_detail),
    path('studio/', views.studio_list),
    path('studio/<int:pk>/', views.studio_detail),
    path("welcome/", views.welcome_view),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),
    path("movies_html/", views.movie_list_html),
    path("movies_html/<int:id>/", views.movie_detail_html),
    path('register/', views.register, name='register'),
    path('movies/monthly/', views.monthly_movies, name='monthly_movies'),

]
