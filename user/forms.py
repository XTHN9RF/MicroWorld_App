from django import forms
from user.models import User, UserProfile

class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(), max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=35)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(),
            'name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
        labels = {
            'email': 'Email',
            'password': 'Password',
            'name': 'First Name',
            'last_name': 'Last Name',
        }
        extra_kwargs = {
            'password': {'write_only': True,'read_only': False},
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','name', 'last_name',]
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True}),
            'name': forms.TextInput(),
            'last_name': forms.TextInput(),
        }
        labels = {
            'name': 'First Name',
            'last_name': 'Last Name',
        }
        extra_kwargs = {
            'email': {'required': False,},
            'name': {'required': False},
            'last_name': {'required': False},
        }


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(),
        }
        labels = {
            'avatar': 'Avatar',
        }
        extra_kwargs = {
            'avatar': {'required': False,},
        }