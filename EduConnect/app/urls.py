from django.urls import path
from . import views

urlspatterns= [
    path('', views.homepage_view, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]