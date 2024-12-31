from django.db import models

# Create your models here.

class Movie(models.Model):
    movieName = models.CharField(max_length=30)
    movieImage = models.ImageField(upload_to='images/')
    movieGenre = models.CharField(max_length=30)
    movieLanguage = models.CharField(max_length=30)
    movieDescription = models.CharField(max_length=300)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    def __str__(self):
        return self.title