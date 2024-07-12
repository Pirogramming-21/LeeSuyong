from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=200)
    openingDate = models.CharField(max_length=20)
    genre = models.CharField(max_length=200)
    score = models.CharField(max_length=20)
    runningtime = models.CharField(max_length=20)
    text = models.TextField()
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=20)

