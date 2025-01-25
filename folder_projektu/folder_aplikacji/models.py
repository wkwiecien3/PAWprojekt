from django.db import models
from django.contrib.auth.models import User

class RATE(models.IntegerChoices):
    ONE = 1, "1"
    TWO = 2, "2"
    THREE = 3, "3"
    FOUR = 4, "4"
    FIVE = 5, "5"
    SIX = 6, "6"
    SEVEN = 7, "7"
    EIGHT = 8, "8"
    NINE = 9, "9"
    TEN = 10, "10"

class MONTHS(models.IntegerChoices):
    JANUARY = 1, "January"
    FEBRUARY = 2, "February"
    MARCH = 3, "March"
    APRIL = 4, "April"
    MAY = 5, "May"
    JUNE = 6, "June"
    JULY = 7, "July"
    AUGUST = 8, "August"
    SEPTEMBER = 9, "September"
    OCTOBER = 10, "October"
    NOVEMBER = 11, "November"
    DECEMBER = 12, "December"

class Genre(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Director(models.Model):
    name = models.CharField(max_length=30, blank = False, null = False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    year_born = models.IntegerField(blank = True, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
class Studio(models.Model):
    name = models.CharField(max_length=100, blank = False, null = False)
    year_of_establishment = models.IntegerField(blank = True, null = True)
    location = models.CharField(max_length=80, blank = False, null = False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Movie(models.Model):
    name = models.CharField(max_length=60)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)   
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True, blank=True)
    director =  models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
    date_watched = models.IntegerField(choices=MONTHS.choices, default=MONTHS.JANUARY)
    rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    review = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Series(models.Model):
    name = models.CharField(max_length=60)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True, blank=True)  
    date_watched = models.IntegerField(choices=MONTHS.choices, default=MONTHS.JANUARY)
    episodes_watched = models.IntegerField()
    rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    review = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
    
