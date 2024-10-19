from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),  # homge page
	path('delete/<str:pk>', views.delete, name='delete')
]