from django.contrib import admin
from django.urls import path, include
from Task import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.index),
    path('api/', include('Task.urls')),   # API routes
    
    
]