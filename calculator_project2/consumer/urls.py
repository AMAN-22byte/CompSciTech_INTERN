# from django.contrib import admin
from django.contrib import views
from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.consume_message, name='consume_message'),
]