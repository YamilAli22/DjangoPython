from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
]
