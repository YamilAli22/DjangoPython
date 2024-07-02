from django.urls import path
from .views import Registro, cerrar_cesion, log_in
urlpatterns = [
    path('', Registro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_cesion, name="cerrar_sesion"),
    path('log_in', log_in, name="log_in"),
]