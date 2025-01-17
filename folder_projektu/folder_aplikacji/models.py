from django.db import models

GENRE = (
    ('F', 'Fantasy'),
    ('R', 'Romance'),
    ('D', 'Drama'),
    ('C', 'Comedy'),
    ('H', 'Horror'),
    ('A', 'Action'),
    ('M', 'Musical'),
    ('T', 'Thriller'),
    ('DOC', 'Documentary'),
    ('SF', 'ScienceFiction'),
    ('AM', 'Animation'),
    ('AD', "Adventure"),
)
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

class Movie(models.Model):
    Name = models.CharField(max_length=60)
    Genre = models.CharField(max_length=3, choices=GENRE) 
    Rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    Review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Name}"
    
class Series(models.Model):
    Name = models.CharField(max_length=60)
    Genre = models.CharField(max_length=3, choices=GENRE)
    Episodes_watched = models.IntegerField()
    Rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    Review = models.TextField(blank=True)

    def __str__(self):
        return f"{self.Name}"