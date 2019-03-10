from django.contrib import admin
from django.urls import path
import . import views

urlpatterns = [
    path('newblog/', views.blogpost, name="newblog"),
]