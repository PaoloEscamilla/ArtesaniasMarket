# tienda/forms.py
from django import forms
from .models import CarritoProducto
from .models import Producto


class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['cantidad']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
