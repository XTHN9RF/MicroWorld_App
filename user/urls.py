from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'user'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'user/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'user/password_change_done.html'), name='password_change_done'),
]
