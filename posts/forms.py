from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """A form to create a new post"""

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Заголовок поста (50 символів максимум)', 'maxlength': '50', 'required': True,
                       'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Вміст поста (250 символів максимум)', 'maxlength': '250', 'required': True,
                       'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
            'image': forms.FileInput(attrs={'placeholder': 'Зображення поста', 'required': True,
                                            'class': 'text-white sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
        }
