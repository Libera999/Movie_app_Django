from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=255) #text based db column

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=255)
    release_year=models.IntegerField(default=None)
    number_in_stock=models.IntegerField(default=None)
    daily_rate=models.FloatField(null=True, blank=True, default=None)
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE, default='')
    date_created=models.DateTimeField(default=timezone.now)
