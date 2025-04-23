from django.db import models
from django.urls import reverse

Genders =(
    ('M','Male'),
    ('F','Female'),
)
# Create your models here
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    release_date = models.DateField(max_length=100)
    genre = models.CharField(max_length=50,null='Unknown')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('movie_detail', args=[str(self.id)])
    
class Characters(models.Model):
        name = models.CharField(max_length=100)
        gender = models.CharField(
            max_length=50,
            choices=Genders,
            default='M',
        )
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
        def __str__(self):
            return f"{self.get_gender_display()} on {self.name}"
        
        class Meta:
            ordering = ['name']
   