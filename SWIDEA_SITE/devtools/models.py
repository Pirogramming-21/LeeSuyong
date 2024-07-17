from django.db import models

# Create your models here.
class Devtools(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    content = models.CharField(max_length=20000)

    def __str__(self):
        return self.name