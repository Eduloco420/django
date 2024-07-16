from .models import *
from rest_framework import viewsets, permissions
from .serializers import * 

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer
    http_method_names = ['get', 'post', 'head','put','delete']

class arteViewSet(viewsets.ModelViewSet):
    queryset = Arte.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = arteSerializer
    http_method_names = ['get', 'post', 'head','put','delete']

class carritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = carritoSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', 'head','put','delete']

class detCarritoViewSet(viewsets.ModelViewSet):
    queryset = Det_carrito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Det_carritoSerilizer    
    http_method_names = ['get', 'post', 'head','put','delete']