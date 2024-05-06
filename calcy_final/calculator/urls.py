from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='calculate'),
    path('get_result/', views.get_result, name='get_result'), 
]