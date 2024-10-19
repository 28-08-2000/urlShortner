from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='indx'),
	path('word', views.word, name='word')
]