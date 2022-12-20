from django.contrib import admin
from django.urls import include, re_path
from django.urls import path, include
from django.urls import include, path
from . import views

urlpatterns = [
   
    path ('', views.TTSHome, name='TTSHome'),
]