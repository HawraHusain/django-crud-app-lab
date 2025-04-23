from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from django.urls import reverse
from .forms import CharactersForm
from django.shortcuts import redirect
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
    characters_form = CharactersForm()
    return render(request, 'movies/details.html', {'movie': movie , 'characters_form': characters_form})
def movie_create(request):
    return render(request, 'movies/create.html')

def add_character(request, movie_id):
    form = CharactersForm(request.POST)
    if form.is_valid():
        new_character = form.save(commit=False)
        new_character.movie_id = movie_id
        new_character.save()
        return redirect('movies:movie_details', movie_id=movie_id)
class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'genre']
    def get_success_url(self):
        return reverse('movies:movie_details', kwargs={'movie_id': self.object.id})

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'genre']
    def get_success_url(self):
        return reverse('movies:movie_details', kwargs={'movie_id': self.object.id})

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'
    def get_success_url(self):
        return reverse('movies:movies')
