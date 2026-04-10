from django.urls import path
# ---> Traemos las Funciones con las Redirecciones a las Páginas Web
from .views import *
from . import views



urlpatterns = [
    # Url , Funcion de Views, Termino para Hipervinculos de HTML
    path('',Inicio, name='Inicio'),
    path("AgregarProd/",AgregarProd,name="agregar"),
    path("verproductos/",verproductos,name="ver"),
    path('editar/<id>/', editar, name="editar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
]
