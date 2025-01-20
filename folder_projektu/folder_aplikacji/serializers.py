from rest_framework import serializers
from .models import Movie, Series, Genre

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
