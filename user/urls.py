from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('home/', views.HomePageView.as_view(), name='home'),
]
