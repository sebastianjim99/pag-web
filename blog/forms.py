from dataclasses import field
from statistics import mode
from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title', 'contents')
