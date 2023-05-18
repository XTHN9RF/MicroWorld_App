from django.urls import path
from django.urls import include


from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('like/', views.PostLikeView.as_view(), name='like'),
    path('own_posts/', views.UserPostView.as_view(), name='own_posts'),
]
