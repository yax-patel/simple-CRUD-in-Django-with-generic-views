from django.db import models

# Create your models here.

class imgForm(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images')
