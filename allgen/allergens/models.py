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
    comment_text = models.TextField(max_length=255)
    reaction = models.BooleanField(default=False)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    created_on = models.DateTimeField(editable=False, null=True)
    edited_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = timezone.now()
        self.edited_on = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('comments', kwargs={'pk':self.pk})

    def __str__(self):
        return '{} Comment posted on {}'.format(self.allergen, self.created_on)