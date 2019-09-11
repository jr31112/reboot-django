from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=5)
    job = models.CharField(max_length=10)