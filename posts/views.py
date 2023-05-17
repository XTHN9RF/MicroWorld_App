from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Post
from .forms import PostForm


class PostCreateView(LoginRequiredMixin, View):
    """A view to list all posts"""

    def get(self, request):
        """Handle GET requests"""
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/create.html', context)

    def post(self, request):
        """Handle POST requests"""
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
        return render(request, 'posts/create.html', {'form': form})


class PostLikeView(View):
    """A view to like a post"""
    def get(self, request):
        return redirect('user:home')
    def post(self, request):
        """Handle POST like functionality"""
        post_id = request.POST.get('id')
        post = Post.objects.get(id=post_id)
        if post.liked_by.filter(id=request.user.id).exists():
            post.liked_by.remove(request.user)
        else:
            post.liked_by.add(request.user)
        return redirect('user:home')
