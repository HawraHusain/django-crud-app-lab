from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from django.urls import reverse
from .forms import CharactersForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

class Log(LogoutView):
    template_name = 'home.html'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movies(request):
    return render(request, 'movies.html')

@login_required
def movie_index(request):
    movies = Movie.objects.filter(user=request.user)
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
    
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('movies:movie_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

class MovieCreate(LoginRequiredMixin,CreateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'genre']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
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
        return reverse('movies:movie_index')
