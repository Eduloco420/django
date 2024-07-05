from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/usuario', usuarioViewSet, 'usuario')
router.register('api/arte', arteViewSet, 'arte')

urlpattern = router.urls