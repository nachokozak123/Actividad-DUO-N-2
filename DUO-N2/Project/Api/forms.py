from django import forms
from .models import Productos

class FormularioProductos(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'input'}),
            'Precio': forms.NumberInput(attrs={'class': 'input'}),
            'Cantidad': forms.NumberInput(attrs={'class': 'input'}),
            'Descripcion': forms.Textarea(attrs={'class': 'input', 'rows': 3}),
            'Fecha': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'Categoria': forms.TextInput(attrs={'class': 'input'}),
            'imagen': forms.FileInput(attrs={'class': 'input'}),
        }

        labels = {
            'Nombre': 'Nombre del Producto',
            'Precio': 'Precio ($)',
            'Cantidad': 'Stock',
            'Descripcion': 'Descripción',
            'Fecha': 'Fecha de ingreso',
            'Categoria': 'Categoría',
            'imagen': 'Imagen del producto'
        }