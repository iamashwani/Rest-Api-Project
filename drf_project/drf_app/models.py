
# Create your models here.
from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.number
        
class SpamNumber(models.Model):
    number = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.number
