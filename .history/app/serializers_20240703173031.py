from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuario
        fields = ('id','nombre','ap_pat','mail','passWord','desc','pfp')
        read_only_fields = ('id',)