from django.db import models

# Create your models here.

class Royal(models.Model):
    fname = models.CharField(max_length=255)
    age = models.IntegerField(max_length=100)

