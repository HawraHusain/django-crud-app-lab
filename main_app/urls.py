# main_app/urls.py
from django.urls import path
from . import views
app_name = 'movies' 

urlpatterns = [
    path('', views.home, name='home'),
    # Other URL patterns here
    path('about/', views.about, name='about'),
    path('movies/', views.movie_index, name='movies'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:movie_id>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:movie_id>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
]
