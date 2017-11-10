import datetime

from django.urls import reverse
from django.utils import timezone


from django.db import models

# Create your models here.


class Allergen(models.Model):
    '''
    This class defines that top 8 allergens, currently hardcoded manually to the DB
    since they're a very specific set of medically dfined top 8 food categories
    '''
    name = models.CharField(max_length=64, unique=True)
    servings = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Comment(models.Model):
    '''
    This is the base class of *eventually* user added comments, each tied to a specific allergen
    by it's foreign key
    '''
    comment_text = models.TextField(max_length=255)
    reaction = models.BooleanField(default=False)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)
    created_on = models.DateTimeField(editable=False, null=True)
    edited_on = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        '''
        auto-defines created_on and edited_on on save
        '''
        if not self.pk:
            self.created_on = timezone.now()
        self.edited_on = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('comments', kwargs={'pk':self.pk})

    def __str__(self):
        '''
        formatting comment listing for admin display
        '''
        return '{} Comment posted on {}'.format(self.allergen, self.created_on)