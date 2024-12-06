from django.db import models
from django.contrib.auth.models import User

# Modelo para los vendedores
class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_tienda = models.CharField(max_length=255)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre_tienda

# Modelo para los productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Este es el campo para las imágenes
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

# Modelo para el carrito de compras
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

# Relación intermedia para el carrito
class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Agregar valor por defecto

    def __str__(self):
        return f"{self.producto.nombre} - Cantidad: {self.cantidad}"
