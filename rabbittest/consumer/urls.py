from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receive-message/', views.receive_message, name='receive_message'),
]
