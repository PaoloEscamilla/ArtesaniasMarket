# tienda/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoProducto
from .forms import AgregarAlCarritoForm
from django.shortcuts import render

def pagina_inicio(request):
    # Recuperar todos los productos
    productos = Producto.objects.all()
    return render(request, 'tienda/pagina_inicio.html', {'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/lista_productos.html', {'productos': productos})

def resetear_cantidad(request, producto_id):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        try:
            carrito_producto = CarritoProducto.objects.get(carrito=carrito, producto_id=producto_id)
            # Resetear la cantidad a 1
            carrito_producto.cantidad = 1
            carrito_producto.save()
        except CarritoProducto.DoesNotExist:
            pass  # Si el producto no está en el carrito, no hacer nada

    return redirect('ver_carrito')  # Redirige de vuelta al carrito

def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        productos_en_carrito = carrito.carritoproducto_set.all()
        productos_con_totales = []
        total_carrito = 0
        for carrito_producto in productos_en_carrito:
            total_producto = carrito_producto.cantidad * carrito_producto.producto.precio
            total_carrito += total_producto
            productos_con_totales.append({
                'producto': carrito_producto.producto,
                'cantidad': carrito_producto.cantidad,
                'total_producto': total_producto
            })
    else:
        productos_con_totales = []
        total_carrito = 0

    return render(request, 'tienda/carrito.html', {
        'productos': productos_con_totales,
        'total_carrito': total_carrito
    })

def actualizar_cantidad(request, producto_id, cantidad):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        try:
            carrito_producto = CarritoProducto.objects.get(carrito=carrito, producto_id=producto_id)
            # Si la cantidad es positiva, aumentamos
            # Si la cantidad es negativa (decremento), restamos
            nueva_cantidad = carrito_producto.cantidad + cantidad

            if nueva_cantidad > 0:  # Asegurarnos de que la cantidad no sea menor que 1
                carrito_producto.cantidad = nueva_cantidad
                carrito_producto.save()
        except CarritoProducto.DoesNotExist:
            pass  # Si el producto no está en el carrito, no hacer nada

    return redirect('ver_carrito')  # Redirige de vuelta al carrito

def agregar_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener o crear el carrito del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    
    # Intentar obtener el producto en el carrito
    carrito_producto, created = CarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)

    if created:
        # Si el producto es nuevo en el carrito, asignamos una cantidad inicial de 1
        carrito_producto.cantidad = 1
    else:
        # Si el producto ya está en el carrito, incrementamos la cantidad
        carrito_producto.cantidad += 1

    # Guardar los cambios en el carrito de productos
    carrito_producto.save()
    
    # Redirigir al carrito para que el usuario vea el contenido
    return redirect('ver_carrito')

def finalizar_compra(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        productos_en_carrito = carrito.carritoproducto_set.all()
        # Calcular el total de cada producto (cantidad * precio)
        total_por_producto = []
        for carrito_producto in productos_en_carrito:
            total = carrito_producto.cantidad * carrito_producto.producto.precio
            total_por_producto.append({
                'carrito_producto': carrito_producto,
                'total': total
            })
        # Calcular el total general
        total_carrito = sum(item['total'] for item in total_por_producto)
    else:
        productos_en_carrito = []
        total_carrito = 0
        total_por_producto = []

    return render(request, 'tienda/finalizar_compra.html', {
        'productos': productos_en_carrito,
        'total_por_producto': total_por_producto,
        'total_carrito': total_carrito
    })
