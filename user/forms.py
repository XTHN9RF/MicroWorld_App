from django import forms
from user.models import User, UserProfile


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': '••••••••',
                                                   'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                                   'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'якийсьтекст@приклад.com',
                                             'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                             'required': True}),
        }

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'якийсьтекст@приклад.com',
                                             'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                             'required': True}),
            'name': forms.TextInput(attrs={'placeholder': 'Введіть ваше ім\'я',
                                           'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                           'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введіть ваше прізвище',
                                                'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                                'required': True}),
            'password': forms.PasswordInput(attrs={'placeholder': '••••••••',
                                                   'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500',
                                                   'required': True}),
        }
        extra_kwargs = {
            'password': {'write_only': True, 'read_only': False},
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', ]
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': True, 'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
            'name': forms.TextInput(attrs={'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'bg-white border sm:text-sm rounded-lg block w-full p-2.5 border-gray-600 placeholder-gray-400 focus:ring-blue-500 focus:border-blue-500'}),
        }
        labels = {
            'name': 'First Name',
            'last_name': 'Last Name',
        }
        extra_kwargs = {
            'email': {'required': False, },
            'name': {'required': False},
            'last_name': {'required': False},
        }


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'text-white'}),
        }
        labels = {
            'avatar': 'Avatar',
        }
        extra_kwargs = {
            'avatar': {'required': False, },
        }
