from django.db import models

# Create your models here.

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Add any other fields you need
    
    def __str__(self):
        return self.title