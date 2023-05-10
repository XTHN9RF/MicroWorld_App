from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """A form to create a new post"""
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Content'}),
            'image': forms.FileInput(attrs={'placeholder': 'Image'}),
        }