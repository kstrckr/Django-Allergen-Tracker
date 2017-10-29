from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Allergen, Comment
# Create your views here.

class AllergenList(generic.ListView):
    model = Allergen
    template_name = 'allergens/index.html'
    context_object_name = 'allergen_list'

    def get_queryset(self):
        return Allergen.objects.all()

class CommentList(generic.ListView):
    model = Comment
    template_name = 'allergens/comments.html'
    context_object_name = 'allergen_comments'

    def get_queryset(self):
        allergen = self.kwargs['allergen']
        return Comment.objects.filter(allergen__name=allergen)

    def get_context_data(self, **kwargs):
        context = super(CommentList, self).get_context_data(**kwargs)
        context['allergen_name'] = self.kwargs['allergen']
        return context

class CommentDelete(generic.DeleteView):
    model = Comment
    
    def get_success_url(self):
        allergen = self.kwargs['allergen']
        return reverse('allergens:comments', kwargs={'allergen':allergen})

