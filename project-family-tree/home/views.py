from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home_screen_view(request):

	return render(request, 'home.html')

def about(request):

	return render(request, 'about.html')