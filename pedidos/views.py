from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from pedidos.models import LineaPedido, Pedido
from carritoapp.carrito import Carrito

# Create your views here.
@login_required(login_url="/autenticacion/log_in")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carrito(request)
    lineas_pedido = list()
    for key, value in carro.carrito.items():
        lineas_pedido.append(LineaPedido(
            
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
            
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido) # método para procesar en "lote", muchos INSERT INTO
    
    enviar_mail(pedido=pedido, lineas_pedido=lineas_pedido, nombre_usuario=request.user.username,
                email_usuario=request.user.email)
    
    messages.success(request, "El pedido se realizo correctamente")
    
    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{
        
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombre_usuario":kwargs.get("nombre_usuario")
        
    })
    mensaje_texto = strip_tags(mensaje)
    from_email="yamil.ali@mi.unc.edu.ar"
    #to=kwargs.get("email_usuario")
    to="yamil.ali@mi.unc.edu.ar"
    send_mail(asunto, mensaje_texto,from_email, [to], html_message=mensaje)