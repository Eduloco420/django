from rest_framework import routers
from .api import *

router.register('api/usuario', usuarioViewSet, 'usuario')
router.register('api/arte', arteViewSet, 'arte')

urlpattern = router.urls