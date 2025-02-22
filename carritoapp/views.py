from django.shortcuts import render, redirect
from .carrito import Carrito
from tiendapp.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.agregar(producto=producto)
    
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.eliminar(producto=producto)
    
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    carrito.restar_unidades(producto=producto)
    
    return redirect("Tienda")

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.vaciar_carrito()
    
    return redirect("Tienda")