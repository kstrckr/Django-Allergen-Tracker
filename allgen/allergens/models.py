import datetime

from django.utils import timezone

from django.db import models

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=64)
    servings = models.IntegerField(default=0)
    
class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    reaction = models.BooleanField(default=False)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
