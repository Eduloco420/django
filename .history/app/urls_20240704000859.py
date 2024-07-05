from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('usuario/', usuarioViewSet, 'usuario')
router.register('arte/', arteViewSet, 'arte')

urlpatterns = router.urls