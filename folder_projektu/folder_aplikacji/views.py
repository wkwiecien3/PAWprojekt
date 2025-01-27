import datetime
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Director, Genre, Movie, Series, Studio
from .permissions import CustomDjangoModelPermissions
from .serializers import UserRegistrationSerializer, directorSerializer, genreSerializer, movieSerializer, seriesSerializer, studioSerializer
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

@api_view(['GET', 'POST'])  
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.filter(creator = request.user)
        serializer = movieSerializer(movie, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':  
        if not request.user.has_perm('app.add_movie'):
            raise PermissionDenied("You do not have permission to add a movie.")
        serializer = movieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(creator = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
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


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
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
        if not request.user.has_perm('app.add_series'):
            raise PermissionDenied("You do not have permission to add any series.")
        serializer = seriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@authentication_classes([TokenAuthentication])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])  
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = genreSerializer(genres, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': 
        if not request.user.has_perm('app.add_genre'):
            raise PermissionDenied("You do not have permission to add a genre.")
        serializer = genreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated]) 
def director_list(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = directorSerializer(director, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        if not request.user.has_perm('app.add_director'):
            raise PermissionDenied("You do not have permission to add a director.")
        serializer = directorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])  
def studio_list(request):
    if request.method == 'GET':
        studio = Studio.objects.all()
        serializer = studioSerializer(studio, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        if not request.user.has_perm('app.add_studio'):
            raise PermissionDenied("You do not have permission to add a studio.")
        serializer = studioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
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
                  "folder_aplikacji/movie/list.html", 
                  {'movies': movies})

def movie_detail_html(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404("Movie with given ID does not exist")

    return render(request, "folder_aplikacji/movie/detail.html", {'movie': movie})

@login_required
@permission_required('folder_aplikacji.view_series')
def series_list_html(request):
    series = Series.objects.all()
    return render(request, 
                  "folder_aplikacji/series/list.html", 
                  {'series': series})

def series_detail_html(request, id):
    try:
        series = Series.objects.get(id=id)
    except Series.DoesNotExist:
        raise Http404("Series with given ID does not exist")

    return render(request, "folder_aplikacji/series/detail.html", {'series': series})

    
class monthlyMovies(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        current_month = timezone.now().month  
        movies = Movie.objects.filter(date_watched=current_month, creator=request.user)  
        if not movies.exists():
            return Response({"message": "No new movies this month"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = movieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class monthlySerieses(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        current_month = timezone.now().month  
        series = Series.objects.filter(date_watched=current_month)  
        if not series.exists():
            return Response({"message": "No new serieses this month"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = seriesSerializer(series, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)