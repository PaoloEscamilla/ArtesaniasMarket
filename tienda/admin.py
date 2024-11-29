# tienda/admin.py
from django.contrib import admin
from .models import Vendedor, Producto, Carrito, CarritoProducto

# Registrar el modelo Vendedor
admin.site.register(Vendedor)

# Registrar el modelo Producto
admin.site.register(Producto)

# Registrar el modelo Carrito
admin.site.register(Carrito)

# Registrar el modelo CarritoProducto
admin.site.register(CarritoProducto)
