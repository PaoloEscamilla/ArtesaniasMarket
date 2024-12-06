from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Producto, Carrito, CarritoProducto, Vendedor
from .forms import AgregarAlCarritoForm, ProductoForm

from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'tienda/pagina_inicio.html')

@login_required
def vista_comprador(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/comprador.html', {'productos': productos})


@login_required
def vista_vendedor(request):
    if hasattr(request.user, 'vendedor'):
        productos = Producto.objects.filter(vendedor=request.user.vendedor)
        return render(request, 'tienda/vendedor.html', {'productos': productos})
    return redirect('vista_comprador')


@login_required
def agregar_producto(request):
    if hasattr(request.user, 'vendedor'):
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.vendedor = request.user.vendedor
                producto.save()
                return redirect('vista_vendedor')
        else:
            form = ProductoForm()
        return render(request, 'tienda/agregar_producto.html', {'form': form})
    return redirect('vista_comprador')


@login_required
def redireccionar_usuario(request):
    if hasattr(request.user, 'vendedor'):
        return redirect('vista_vendedor')
    return redirect('vista_comprador')


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})


def ver_carrito(request):
    # Obtiene el carrito del usuario actual
    carrito = Carrito.objects.filter(usuario=request.user).first()
    productos_con_totales = []
    total_carrito = 0
    
    if carrito:
        productos_en_carrito = carrito.carritoproducto_set.all()
        for carrito_producto in productos_en_carrito:
            total_producto = carrito_producto.cantidad * carrito_producto.producto.precio
            total_carrito += total_producto
            productos_con_totales.append({
                'producto': carrito_producto.producto,
                'cantidad': carrito_producto.cantidad,
                'total_producto': total_producto
            })

    return render(request, 'tienda/carrito.html', {
        'productos': productos_con_totales,
        'total_carrito': total_carrito
    })

def agregar_carrito(request, producto_id):
    # Verificamos si el usuario está autenticado
    if not request.user.is_authenticated:
        return redirect('login')  # Redirigir al login si no está autenticado

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
    
    # Mantener al usuario en la página actual de productos
    return redirect('vista_comprador')  # Redirige de vuelta a la vista de los productos

@login_required
def resetear_cantidad(request, producto_id):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        try:
            item = CarritoProducto.objects.get(carrito=carrito, producto_id=producto_id)
            item.cantidad = 1
            item.save()
        except CarritoProducto.DoesNotExist:
            pass
    return redirect('ver_carrito')


@login_required
def actualizar_cantidad(request, producto_id, accion):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        try:
            item = CarritoProducto.objects.get(carrito=carrito, producto_id=producto_id)
            if accion == 'incrementar':
                item.cantidad += 1
            elif accion == 'decrementar' and item.cantidad > 1:
                item.cantidad -= 1
            item.save()
        except CarritoProducto.DoesNotExist:
            pass
    return redirect('ver_carrito')


@login_required
def eliminar_producto_carrito(request, producto_id):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        try:
            item = CarritoProducto.objects.get(carrito=carrito, producto_id=producto_id)
            item.delete()
        except CarritoProducto.DoesNotExist:
            pass
    return redirect('ver_carrito')

@login_required
def eliminar_producto(request, producto_id):
    # Verificar que el usuario es un vendedor
    if hasattr(request.user, 'vendedor'):
        producto = get_object_or_404(Producto, id=producto_id)
        # Verificar que el producto pertenece al vendedor autenticado
        if producto.vendedor == request.user.vendedor:
            producto.delete()
            return redirect('vista_vendedor')  # Redirige al vendedor después de eliminar el producto
    return redirect('vista_comprador')  # Si no es vendedor, redirige al comprador


@login_required
def finalizar_compra(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    productos_en_carrito = []
    total_carrito = 0

    if carrito:
        productos_en_carrito = carrito.carritoproducto_set.all()
        total_carrito = sum(item.cantidad * item.producto.precio for item in productos_en_carrito)

    return render(request, 'tienda/finalizar_compra.html', {
        'productos': productos_en_carrito,
        'total_carrito': total_carrito
    })


@login_required
def productos_vendedor(request):
    if hasattr(request.user, 'vendedor'):
        productos = Producto.objects.filter(vendedor=request.user.vendedor)
        return render(request, 'tienda/productos_vendedor.html', {'productos': productos})
    return redirect('vista_comprador')


@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if hasattr(request.user, 'vendedor') and producto.vendedor == request.user.vendedor:
        if request.method == 'POST':
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('vista_vendedor')
        else:
            form = ProductoForm(instance=producto)
        return render(request, 'tienda/editar_producto.html', {'form': form, 'producto': producto})
    return redirect('vista_comprador')
