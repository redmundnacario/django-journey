from django.views.generic import ListView
from .models import command

# from django.shortcuts import render

# Create your views here.

class HomePageView(ListView):
    model = command
    template_name = 'home.html'
