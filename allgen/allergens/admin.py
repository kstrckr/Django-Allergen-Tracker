from django.contrib import admin

from .models import Allergen, Comment
# Register your models here.

admin.site.register(Allergen)
admin.site.register(Comment)