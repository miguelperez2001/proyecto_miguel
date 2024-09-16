from django.shortcuts import render,redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    context= {'form' : form}
    return render(request, 'registro.html', context)

def login(request):
    return render(request,'iniciar-sesion.html')

def logout(request):
    return render(request,'cerrar-sesion.html')

# Create your views here.
