from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Boleta, Cliente, Movimiento, Producto

from . import views

router = DefaultRouter()
router.register('productos', views.ProductoViewSet)
router.register('clientes', views.ClienteViewSet)
router.register('movimientos', views.MovimientoViewSet)
router.register('boletas', views.BoletaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
