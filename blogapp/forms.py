from django import forms
from .models import Blogpostmodel, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Blogpostmodel
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']