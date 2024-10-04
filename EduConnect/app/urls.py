from django.urls import path
from . import views

urlspatterns= [
    path('', views.homepage_view, name='homepage'),
    
]