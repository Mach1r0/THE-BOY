from django.db import models
from django.utils import timezone
from Artist.models import Artist
from Genrer.models import Genrer 

class Album(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    ReleaseDate = models.DateTimeField(default=timezone.now)
    price = models.FloatField()
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=False, null=False)
    genres = models.ManyToManyField(Genrer, blank=True) 
    picture = models.ImageField(upload_to='albums-img/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
