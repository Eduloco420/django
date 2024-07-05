from rest_framework import routers
from .api import *

routers.register('api/usuario', usuarioViewSet, 'usuario')
routers.register('api/arte', arteViewSet, 'arte')

urlpattern = router.urls