from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('nom','ap_pat','mail','password','desc','pfp','is_staff')
        
class arteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arte    
        fields = ('id','nom_arte','imagen_url','precio','desc','tec_usada','etiquetas','aprobado','vendido')
        