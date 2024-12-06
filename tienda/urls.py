from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.pagina_inicio, name='pagina_inicio'),

    # Funcionalidades del carrito
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('actualizar_cantidad/<int:producto_id>/<str:accion>/', views.actualizar_cantidad, name='actualizar_cantidad'),
    path('resetear_cantidad/<int:producto_id>/', views.resetear_cantidad, name='resetear_cantidad'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_producto_carrito, name='eliminar_producto_carrito'),

    # Autenticación
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='pagina_inicio'), name='logout'),
    path('registro/', views.registro, name='registro'),

    # Redirección según usuario
    path('redirect/', views.redireccionar_usuario, name='redireccionar_usuario'),

    # Vistas para roles
    path('comprador/', views.vista_comprador, name='vista_comprador'),
    path('vendedor/', views.vista_vendedor, name='vista_vendedor'),
    path('vendedor/agregar/', views.agregar_producto, name='agregar_producto'),
    path('vendedor/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('vendedor/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
]
