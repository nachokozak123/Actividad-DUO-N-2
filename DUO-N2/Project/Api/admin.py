from django.contrib import admin
from .models import Productos

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('Codigo', 'Nombre', 'Precio', 'Cantidad', 'Categoria', 'Fecha')
    search_fields = ('Nombre', 'Categoria')
    list_filter = ('Categoria', 'Fecha')