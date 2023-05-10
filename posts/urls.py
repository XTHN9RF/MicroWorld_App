from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='create'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
