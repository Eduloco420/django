from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id','nombre','ap_pat','mail','passWord','desc','pfp','admin')
        read_only_fields = ('id',)
        
class arteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arte    
        fields = ('id','nom_arte','imagen_url','precio','desc','tec_usada','etiquetas','aprobado','vendido')
        