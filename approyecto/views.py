from django.shortcuts import render
from carritoapp.carrito import Carrito

# Create your views here.

def home(request):
    carrito = Carrito(request)
    return render(request, "approyecto/home.html")
