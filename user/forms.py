from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(), max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=35)
