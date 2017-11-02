from django import forms

class CommentCreateForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea)
    reaction = forms.BooleanField()
    # allergen = 
    created_on = forms.DateTimeField()
