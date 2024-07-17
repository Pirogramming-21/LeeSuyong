from django.db import models

# Create your models here.
from devtools.models import Devtools


class Ideas(models.Model):
    title = models.CharField(max_length= 100)
    ideaImage = models.ImageField(null=True, upload_to='images/', )
    content = models.CharField(max_length= 20000)
    interset = models.IntegerField(default=0)
    devtool = models.ForeignKey(Devtools, on_delete=models.CASCADE, null=True)
    # likeStar = models.BooleanField(default=False)

    def __str__(self):
        return self.title
