from django.contrib import admin
from django.urls import path
from news.views import index

urlpatterns = [
    path('index', index),
]
