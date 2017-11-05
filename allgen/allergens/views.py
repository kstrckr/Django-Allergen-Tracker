from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Allergen, Comment
from . import forms
# Create your views here.


class AllergenList(generic.ListView):
    model = Allergen
    template_name = 'allergens/index.html'
    context_object_name = 'allergen_list'

    def get_queryset(self):
        return Allergen.objects.all().order_by('name')

class CreateComment(generic.CreateView):
    model = Comment
    fields = [
        'comment_text',
        'reaction',
        ]
    context_object_name = 'allergen_details'

    def get_context_data(self, **kwargs):
        context = super(CreateComment, self).get_context_data(**kwargs)
        context['allergen_name'] = self.kwargs['allergen']
        return context

    def form_valid(self, form):
        allergen_from_url = self.kwargs['allergen']
        allergen_instance = Allergen.objects.get(name__exact=allergen_from_url)
        form.instance.allergen = allergen_instance
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        allergen = self.kwargs['allergen']
        return reverse('allergens:comments', kwargs={'allergen':allergen})

class CommentUpdate(generic.UpdateView):
    pass
    model = Comment
    fields = [
        'comment_text',
        'reaction',
    ]

    def get_success_url(self):
        allergen = self.kwargs['allergen']
        return reverse('allergens:comments', kwargs={'allergen':allergen})

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
