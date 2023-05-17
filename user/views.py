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
from posts.forms import CommentForm

from .models import User
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
        # return render(request, 'user/login.html', {'form': form})


class HomePageView(LoginRequiredMixin, View):
    """Handles logic of home page view"""

    def get(self, request):
        """Handles GET requests"""
        user = request.user
        posts = Post.objects.filter(user=user)
        comment_form = CommentForm()
        context = {'posts': posts, 'user': user, 'comment_form': comment_form, }
        return render(request, 'user/index.html', context)

    def post(self, request):
        """Handles POST requests"""
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(id=request.POST['post_id'])
            comment.save()
            return redirect('user:home')
        return HttpResponse('Неправильні дані', status=401)


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
            return redirect('user:login')
        return render(request, 'user/register.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, View):
    """Handles logic of user update view"""
    form = UserUpdateForm

    def get(self, request):
        """Handles GET requests"""
        user_form = self.form(instance=request.user)
        context = {'user_form': user_form}
        return render(request, 'user/update.html', context)

    def post(self, request):
        """Handles POST requests"""
        user_form = self.form(instance=request.user, data=request.POST, files=request.FILES)
        context = {'user_form': user_form, }
        if user_form.is_valid():
            user_form.save()
            return redirect('user:home')
        return render(request, 'user/update.html', context)


class UserProfileView(LoginRequiredMixin, View):
    """Handles logic of user profile view"""

    def get(self, request):
        """Handles GET requests"""
        user = request.user
        comment_form = CommentForm()
        if Post.objects.filter(user=user).exists():
            post = Post.objects.filter(user=user).latest('date_posted')
            context = {'user': user, 'post': post, 'comment_form': comment_form, }
        else:
            context = {'user': user, 'comment_form': comment_form, }
        return render(request, 'user/profile.html', context)

    def post(self, request):
        """Handles POST requests"""
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(id=request.POST['post_id'])
            comment.save()
            return redirect('user:profile')
        return HttpResponse('Неправильні дані', status=401)
