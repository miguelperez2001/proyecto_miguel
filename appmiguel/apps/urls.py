from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='iniciar-sesion.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cerrar-sesion.html'), name='logout'),
    path('', views.home, name='home'),
]