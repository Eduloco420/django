from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('usuario', usuarioViewSet, 'usuario')
router.register('arte', arteViewSet, 'arte')
router.register('carrito', CarritoViewSet, 'carrito')

urlpatterns = router.urls