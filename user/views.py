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

    def post(self, request):
        """Handles GET requests"""
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Logged in sucessfullyy', status=200)
            else:
                return HttpResponse('Invalid username or password', status=401)
        return render(request, 'user/login.html', {'form': form})
