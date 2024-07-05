from .models import *
from rest_framework import viewsets, permissions
from .serializers import * 

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer
    http_method_names = ['GET', 'POST', 'HEAD','PUT']

class arteViewSet(viewsets.ModelViewSet):
    queryset = Arte.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer
    http_method_names = ['GET', 'POST', 'HEAD','PUT','DELETE']
