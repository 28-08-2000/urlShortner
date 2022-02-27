from django.urls import path
from . import views

urlpatterns = [
	# for '' url show index view 
	path('', views.index, name='index')
]