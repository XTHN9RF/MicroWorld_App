from django.urls import path
from . import views


app_name = 'chat'

urlpatterns = [
    path('', views.InboxView.as_view(), name='index'),
    path('message/<str:pk>/', views.MessageView.as_view(), name='message'),
]
