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
from .forms import AvatarUpdateForm

from .models import UserProfile, User
from posts.models import Post


class LoginView(View):
    """Handles login functionallity for users"""
    form = LoginForm

    def get(self, request):
        """Handles GET requests"""
        return render(request, 'user/login.html', {'form': self.form})

    def post(self, request):
        """Handles GET requests"""
        form = self.form(request.POST)
        data = form.data
        user = authenticate(request, username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return redirect('user:home')
        else:
            return HttpResponse('Неправильні пароль або ім\'я користувача', status=401)
        #return render(request, 'user/login.html', {'form': form})


class HomePageView(LoginRequiredMixin, View):
    """Handles logic of home page view"""

    def get(self, request):
        """Handles GET requests"""
        user = request.user
        posts = Post.objects.filter(user=user)
        return render(request, 'user/index.html', {'posts': posts})


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
            return redirect('user:login')
        return render(request, 'user/register.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, View):
    """Handles logic of user update view"""
    form = UserUpdateForm
    avatar_form = AvatarUpdateForm

    def get(self, request):
        """Handles GET requests"""
        user_form = self.form(instance=request.user)
        avatar_form = self.avatar_form(instance=request.user)
        return render(request, 'user/update.html', {'user_form': user_form, 'avatar_form': avatar_form})

    def post(self, request):
        """Handles POST requests"""
        user_form = self.form(instance=request.user, data=request.POST)
        avatar_form = self.avatar_form(instance=request.user, files=request.FILES)
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return redirect('user:home')
        return render(request, 'user/update.html', {'user_form': user_form, 'avatar_form': avatar_form})
