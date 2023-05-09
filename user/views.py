from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

from .forms import LoginForm
from .forms import RegisterForm
from .forms import UserUpdateForm

from . models import UserProfile

class LoginView(View):
    """Handles login functionallity for users"""
    form = LoginForm

    def get(self, request):
        """Handles GET requests"""
        return render(request, 'user/login.html', {'form': self.form})

    def post(self, request):
        """Handles GET requests"""
        form = self.form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Ви успішно увійшли до системи', status=200)
            else:
                return HttpResponse('Неправильні пароль або ім\'я користувача', status=401)
        return render(request, 'user/login.html', {'form': form})


class HomePageView(LoginRequiredMixin, View):
    """Handles logic of home page view"""

    def get(self, request):
        """Handles GET requests"""
        return render(request, 'user/home.html')


class RegisterView(View):
    """Handles logic of registration view"""
    form = RegisterForm

    def get(self, request):
        """Handles GET requests"""
        return render(request, 'user/register.html', {'form': self.form})

    def post(self, request):
        """Handles POST requests"""
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            UserProfile.objects.create(user=user)
            return redirect('login/')
        return render(request, 'user/register.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, View):
    """Handles logic of user update view"""
    form = UserUpdateForm

    def get(self, request):
        """Handles GET requests"""
        return render(request, 'user/update.html', {'form': self.form})

    def post(self, request):
        """Handles POST requests"""
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            user.name = data['name']
            user.last_name = data['last_name']
            if data['avatar']:
                user.avatar = data['avatar']
            user.save()
            return HttpResponse('Ви успішно оновили свій профіль', status=200)
        return render(request, 'user/update.html', {'form': form})