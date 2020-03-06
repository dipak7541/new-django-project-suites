from django.db import models



class ManxekoBichar(models.Model):
    name = models.CharField(max_length=20)
    comments= models.CharField(max_length=200)
    date= models.DateField()



# Create your models here.
