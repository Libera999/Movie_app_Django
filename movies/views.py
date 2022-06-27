from django.http import HttpResponse
from django.shortcuts import render #render template
from .models import Movie

# Create your views here.
def index(request):
    movies=Movie.objects.all() #SELECT * FROM movies_movie - gets a list of movies from the DB
    output=render(request,'movies/index.html',{'movies': movies}) 
    
    #Movie.objects.filter(release_year=1999) #SELECT * FROM movies_movie WHERE 
    #Movie.objects.get(id=1) #SELECT * FROM movies_movie
    
    return HttpResponse(output)

def detail(request, movie_id):
    movie=Movie.objects.get(pk=movie_id)

    return render(request, 'movies/detail.html',{'movies': movie})
