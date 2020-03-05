from django.db import models


class PeopleSay(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=20)
    comments= models.TextField()
    

# Create your models here.
