from django.db import models

# Create your models here.

class City(models.Model):
    def __str__(self):
        return self.city
    city=models.CharField(max_length=30)

