from django.urls import path
from . import views

urlpatterns = [
	# for '' url show index view 
	path('', views.index, name='index'),
	path('create', views.create, name='create'),

	# a dynamic url
	path('<str:pk>', views.go, name='go')
]