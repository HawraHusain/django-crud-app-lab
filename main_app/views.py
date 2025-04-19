from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Movie
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movies(request):
    return render(request, 'movies.html')
def movie_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movie_details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})
def movie_create(request):
    return render(request, 'movies/create.html')


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'genre']
    success_url = '/movies.html/'
