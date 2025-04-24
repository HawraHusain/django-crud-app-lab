# main_app/urls.py
from django.urls import path
from . import views

app_name = 'movies' 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # Other URL patterns here
    path('about/', views.about, name='about'),
    path('movies/', views.movie_index, name='movie_index'),
    path('movies/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movies/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('movies/<int:movie_id>/add-character/', views.add_character, name='add-character'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='movies:home'), name='logout'),
]
