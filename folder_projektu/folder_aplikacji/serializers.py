from wsgiref import validate
from rest_framework import serializers
from .models import Movie, Series, RATE, GENRE, MONTHS


class MovieSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Genre = serializers.ChoiceField(choices=GENRE, default=GENRE[0][0])
    Date_watched = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.JANUARY)
    Rating = serializers.ChoiceField(choices=RATE.choices, default=RATE.ONE) 
    Review = serializers.CharField(allow_blank=True, allow_null=True)

    def validate_Name(self, value):

        if not value.istitle():
            raise serializers.ValidationError(
                "Movie's name should start with a capital letter!",
            )
        return value

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Genre = validated_data.get('Genre', instance.Genre)
        instance.Date_watched = validated_data.get('Date_watched', instance.Date_watched)
        instance.Rating = validated_data.get('Rating', instance.Rating)
        instance.Review = validated_data.get('Review', instance.Review)
        instance.save()
        return instance
    
class SeriesSerializer(serializers.Serializer):
    Name = serializers.CharField(required=True)
    Genre = serializers.ChoiceField(choices=GENRE, default=GENRE[0][0])
    Date_watched = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.JANUARY) 
    Episodes_watched = serializers.IntegerField()
    Rating = serializers.ChoiceField(choices=RATE.choices, default=RATE.ONE)  
    Review = serializers.CharField(allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Series.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Genre = validated_data.get('Genre', instance.Genre)
        instance.Date_watched = validated_data.get('Date_watched', instance.Date_watched)
        instance.Episodes_watched = validated_data.get('Episodes_watched', instance.Episodes_watched)
        instance.Rating = validated_data.get('Rating', instance.Rating)
        instance.Review = validated_data.get('Review', instance.Review)
        instance.save()
        return instance
    