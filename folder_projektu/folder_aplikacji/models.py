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

class Movie(models.Model):
    Name = models.CharField(max_length=60)
    Genre = models.CharField(max_length=3, choices=GENRE)
    Date_watched = models.IntegerField(choices = MONTHS.choices, default=MONTHS.JANUARY)
    Rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    Review = models.CharField(max_length=20000, blank=True)

    def __str__(self):
        return f"{self.Name}"
    
class Series(models.Model):
    Name = models.CharField(max_length=60)
    Genre = models.CharField(max_length=3, choices=GENRE)
    Date_watched = models.IntegerField(choices = MONTHS.choices, default=MONTHS.JANUARY)
    Episodes_watched = models.IntegerField()
    Rating = models.IntegerField(choices=RATE.choices, default=RATE.ONE)
    Review = models.CharField(max_length=20000, blank=True)

    def __str__(self):
        return f"{self.Name}"