from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nom','ap_pat','email','password','desc','pfp','is_staff')
        
class arteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arte    
        fields = ('id','artista','nom_arte','imagen_url','precio','desc','tec_usada','etiquetas','aprobado','vendido')
        
class carritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrito
        fields = ('id','usuario')

class Det_carritoSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Det_carrito
        fields = ('id', 'carrito', 'arte')