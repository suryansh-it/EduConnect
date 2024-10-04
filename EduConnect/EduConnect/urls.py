"""
URL configuration for EduConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),        # Admin panel for user and content management.
    path('' , include('app.urls')),
    path('', views.homepage_view, name='home'),  # Root URL, points to homepage
    path('accounts/', include('django.contrib.auth.urls'))  
#This automatically includes views for login, logout, password reset, and more. The default URLs are:
#/accounts/login/
#/accounts/logout/
#/accounts/password_change/
#/accounts/password_reset/


]
