from django.shortcuts import render
from apps.models import Videojuego, Serie, Cocina

def home(request):

    return render(request, "home.html",{})

def posts(request):

    return render(request, "posts.html",{})

def videojuegos(request):
    query = request.GET.get('q')
    videojuegos=Videojuego.objects.all()
    if query:
        videojuegos = videojuegos.filter(nombre__icontains=query)
    
    return render(request, "videojuegos.html",{"videojuegos":videojuegos})

def cocina(request):
    query = request.GET.get('q')
    cocina=Cocina.objects.all()
    if query:
        cocina = cocina.filter(nombre__icontains=query)
    return render(request, "cocina.html",{"cocina":cocina})

def series(request):
    query = request.GET.get('q')
    series=Serie.objects.all()
    if query:
        series = series.filter(nombre__icontains=query)
    return render(request, "series.html",{"series":series})

def proyecto(request):

    return render(request, "proyecto.html",{})