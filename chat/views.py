from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'chat/index.html'