from django.urls import path
from . import views

urlpatterns = [
    path('royal1/',views.royal1,name='royal1'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
]
