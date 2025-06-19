from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('temp/', views.getData, name='temp'),
    path('basic/', views.django_basic, name='basic'),
]
