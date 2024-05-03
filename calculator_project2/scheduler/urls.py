from django.contrib import admin
from django.contrib import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schedule/', views.schedule_tasks, name='schedule_tasks'),
]