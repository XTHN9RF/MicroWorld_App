from django import forms


class LoginForm(forms.Form):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(), max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=35)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Email',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        extra_kwargs = {
            'password': {'write_only': True,'read_only': True},
        }
