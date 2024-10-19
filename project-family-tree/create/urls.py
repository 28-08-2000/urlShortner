from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('create/relation/', views.create_relation, name='create_relation'),
    path('create/delete/<str:id>/', views.delete_ind, name='delete_ind'),
]
