from django.urls import path
from . import views

urlpatterns = [
    path('royal1/',views.royal1,name='royal1'),
    path('royal2/',views.royal2,name='royal2'),
]
