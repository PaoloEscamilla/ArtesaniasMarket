# tienda/forms.py
from django import forms
from .models import CarritoProducto

class AgregarAlCarritoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['cantidad']
