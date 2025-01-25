from rest_framework import serializers
from .models import Director, Movie, Series, Genre, Studio

class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

    id = serializers.CharField(required = True)

    def validate_id(self, value):
        return value.upper()

class movieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    name = serializers.CharField(required = True)
    
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'studio', 'director', 'date_watched', 'rating', 'review']

    def validate_name(self, value):
        if not value.istitle():
            raise serializers.ValidationError(
                "Movie's name should start with a capital letter!"
            )
        return value

    def create(self, validated_data):
        genre = validated_data.pop('genre')  
        movie = Movie.objects.create(genre=genre, **validated_data)
        return movie

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre', None)
        if genre:
            instance.genre = genre
        instance.studio = validated_data.get('studio', instance.studio)
        instance.director = validated_data.get('director', instance.director)
        instance.name = validated_data.get('name', instance.name)
        instance.date_watched = validated_data.get('date_watched', instance.date_watched)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.review = validated_data.get('review', instance.review)
        instance.save()
        return instance

class seriesSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    class Meta:
        model = Series
        fields = ['name', 'genre', 'studio', 'date_watched', 'episodes_watched', 'rating', 'review']

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        series = Series.objects.create(genre=genre, **validated_data)
        return series

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre', None)
        if genre:
            instance.genre = genre
        instance.studio = validated_data.get('studio', instance.studio)
        instance.name = validated_data.get('name', instance.name)
        instance.date_watched = validated_data.get('date_watched', instance.date_watched)
        instance.episodes_watched = validated_data.get('episodes_watched', instance.episodes_watched)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.review = validated_data.get('review', instance.review)
        instance.save()
        return instance
    
class directorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'surname', 'year_born']

    def create(self, validated_data):
        director = Director.objects.create(**validated_data)
        return director

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.year_born = validated_data.get('year_born', instance.year_born)
        instance.save()
        return instance

class studioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Studio
        fields = ['name', 'year_of_establishment', 'location']

    def create(self, validated_data): 
        studio = Studio.objects.create(**validated_data)
        return studio

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.year_of_establishment = validated_data.get('year_of_establishment', instance.year_of_establishment)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance