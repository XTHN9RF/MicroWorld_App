from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm


class LoginView(View):
    """Handles login functionallity for users"""

    def get(self, request):
        """Handles GET requests"""
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
