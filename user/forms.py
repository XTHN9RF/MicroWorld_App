from django import forms
from user.models import User

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
