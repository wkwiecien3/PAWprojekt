from rest_framework import serializers
from .models import Director, Movie, Series, Genre

class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

class movieSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = ['name', 'genre', 'date_watched', 'rating', 'review']

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
        fields = ['name', 'genre', 'date_watched', 'episodes_watched', 'rating', 'review']

    def create(self, validated_data):
        genre = validated_data.pop('genre')
        series = Series.objects.create(genre=genre, **validated_data)
        return series

    def update(self, instance, validated_data):
        genre = validated_data.pop('genre', None)
        if genre:
            instance.genre = genre
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
