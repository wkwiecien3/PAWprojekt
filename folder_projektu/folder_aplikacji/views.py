import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Director, Genre, Movie, Series, Studio
from .permissions import CustomDjangoModelPermissions
from .serializers import directorSerializer, genreSerializer, movieSerializer, seriesSerializer, studioSerializer
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied




def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Hello! </br>
        Current date and time: {now}.
        </body></html>"""
    return HttpResponse(html)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully!"})

@api_view(['GET'])  
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = movieSerializer(movie, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = movieSerializer(movie)
        return Response(serializer.data)
    
@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def movie_update(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = movieSerializer(movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'POST':  
    #     serializer = movieSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_delete(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:  
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST']) 
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])   
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

@api_view(['GET', 'DELETE'])
def series_detail(request, pk):
    try:
        series = Series.objects.get(pk=pk)
    except Series.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = seriesSerializer(series)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def series_search(request, substring):
    series = Series.objects.filter(name__icontains = substring)
    serializer = seriesSerializer(series, many = True)
    return Response(serializer.data)

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

@api_view(['GET', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = genreSerializer(genre)
        return Response(serializer.data)

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
    

@login_required
@permission_required('folder_aplikacji.view_movie')
def movie_list_html(request):
    movies = Movie.objects.all()
    return render(request, 
                  "folder_aplikacji/movies/list.html", 
                  {'movies': movies})

def movie_detail_html(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404("Movie with given ID does not exist")

    return render(request, "folder_aplikacji/movies/detail.html", {'movie': movie})

    
class GenreMemberView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        movie = Movie.objects.filter(genre = genre)
        serializer = movieSerializer(movie, many = True)
        return Response(serializer.data)
    
class StudioDetail(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    def get_queryset(self):
        return Studio.objects.all()

    def get_object(self, pk):
        try:
            return Studio.objects.get(pk=pk)
        except Studio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        studio = self.get_object(pk)
        serializer = studioSerializer(studio)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        studio = self.get_object(pk)
        studio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)