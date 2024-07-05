from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('nombre','ap_pat','mail','passWord','desc','pfp','admin')
        
    def create(self, validated_data):
        password = validated_data.pop('passWord')
        user = Usuario(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
        
class arteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arte    
        fields = ('id','nom_arte','imagen_url','precio','desc','tec_usada','etiquetas','aprobado','vendido')
        