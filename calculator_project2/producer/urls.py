from django.contrib import admin
from django.urls import path
from .views import add

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('add/', add, name='add'),
]