from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, ClienteViewSet, MovimientoViewSet, BoletaViewSet

router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('clientes', ClienteViewSet)
router.register('movimientos', MovimientoViewSet)
router.register('boletas', BoletaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
