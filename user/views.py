from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse

from .forms import LoginForm


class LoginView(View):
    """Handles login functionallity for users"""
    form = LoginForm()

    def get(self, request):
        """Handles GET requests"""
        form = self.form
        return render(request, 'user/login.html', {'form': form})


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
