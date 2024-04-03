"""
Definition of urls for Question1.
"""

from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
]
