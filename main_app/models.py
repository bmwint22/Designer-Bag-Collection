from django.db import models

class Bag(models.Model):
    brand = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    texture = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    
    def __str__(self):
        return self.brand
    
