from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Series
from .serializers import MovieSerializer, SeriesSerializer

@api_view(['GET'])
def Movie_list(request):
    if request.method == 'GET':
        persons = Movie.objects.all()
        serializer = MovieSerializer(Movie, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def Movie_detail(request, pk):
    try:
        Movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(Movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerializer(Movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Series_list(request):
    if request.method == 'GET':
        Movie = Movie.objects.all()
        serializer = MovieSerializer(Movie, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def Series_detail(request, pk):
    try:
        Series = Series.objects.get(pk=pk)
    except Series.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        Series = Series.objects.get(pk=pk)
        serializer = SeriesSerializer(Series)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SeriesSerializer(Series, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)