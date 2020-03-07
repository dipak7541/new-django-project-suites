from django.db import models
from django.utils.timezone import now



class ManxekoBichar(models.Model):
    name = models.CharField(max_length=20)
    comments = models.CharField(max_length=200)
    date = models.DateField()

class ContactDetails(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phoneno = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateTimeField(default=now, editable=False)


# Create your models here.
