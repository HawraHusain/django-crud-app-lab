from django.contrib import admin

# Register your models here.
from .models import Movie , Characters

admin.site.register(Movie)
admin.site.register(Characters)