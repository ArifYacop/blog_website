from django.db import models

# Create your models here.
class post(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    