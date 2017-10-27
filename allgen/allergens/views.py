from django.shortcuts import render
from django.views import generic

from .models import Allergen, Comment
# Create your views here.

class allergen_list(generic.ListView):
    template_name = 'allergens/index.html'
    context_object_name = 'allergen_list'

    def get_queryset(self):
        return Allergen.objects.all()

class DetailView(generic.ListView):
    model = Comment
    template_name = 'allergens/comments.html'
    context_object_name = 'allergen_comments'

    def get_queryset(self):
        allergen = self.kwargs['allergen']
        return Comment.objects.filter(allergen__name=allergen)