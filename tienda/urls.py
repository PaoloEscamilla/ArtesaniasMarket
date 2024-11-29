# tienda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),  # Página de inicio
    path('productos/', views.lista_productos, name='lista_productos'),  # Ruta para la lista de productos
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('actualizar_cantidad/<int:producto_id>/<int:cantidad>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('resetear_cantidad/<int:producto_id>/', views.resetear_cantidad, name='resetear_cantidad'),  # Ruta para resetear la cantidad
]
