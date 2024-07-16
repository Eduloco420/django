from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('usuario', usuarioViewSet, 'usuario')
router.register('arte', arteViewSet, 'arte')
router.register('carrito', carritoViewSet, 'carrito')
router.register('det_carrito', detCarritoViewSet, 'det_carrito')

urlpatterns = router.urls