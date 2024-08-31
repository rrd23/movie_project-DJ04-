from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
