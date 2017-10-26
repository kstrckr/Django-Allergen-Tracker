import datetime

from django.utils import timezone

from django.db import models

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=64, unique=True)
    servings = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    comment_text = models.CharField(max_length=255)
    reaction = models.BooleanField(default=False)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    created_on = models.DateTimeField(timezone.now())

    def __str__(self):
        return '{} Comment posted on {}'.format(self.allergen, self.created_on)