from django.contrib import admin
from django.urls import path, include
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('', lambda request: redirect('home', permanent=True)),
    path('posts/', views.posts, name='posts'),
    path('posts/videojuegos', views.videojuegos, name='videojuegos'),
    path('posts/cocina', views.cocina, name='cocina'),
    path('posts/series', views.series, name='series'),
    path('proyecto/', views.proyecto, name='proyecto'),
]