from django.urls import path, include
from tiendapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.tienda, name="Tienda"),
]
