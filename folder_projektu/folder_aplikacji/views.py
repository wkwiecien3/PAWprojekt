from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Genre, Movie, Series, Studio
from .serializers import directorSerializer, genreSerializer, movieSerializer, seriesSerializer, studioSerializer

@api_view(['GET', 'POST'])  
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = movieSerializer(movie, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = movieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = movieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = movieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) 
def series_list(request):
    if request.method == 'GET':
        series = Series.objects.all()
        serializer = seriesSerializer(series, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  
        serializer = seriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def series_detail(request, pk):
    try:
        series = Series.objects.get(pk=pk)
    except Series.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = seriesSerializer(series)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = seriesSerializer(series, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])  
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = genreSerializer(genres, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = genreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = genreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = genreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])  
def director_list(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = directorSerializer(director, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = directorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, pk):
    try:
        director = Director.objects.get(pk=pk)
    except Director.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = directorSerializer(director)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = directorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])  
def studio_list(request):
    if request.method == 'GET':
        studio = Studio.objects.all()
        serializer = studioSerializer(studio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = studioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studio_detail(request, pk):
    try:
        studio = Studio.objects.get(pk=pk)
    except Studio.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studioSerializer(studio)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = studioSerializer(studio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        studio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    