from django.urls import path
from .views import home_screen_view, about

urlpatterns = [
	path('', home_screen_view, name='home'),
	path('about', about, name='about')
]