from rest_framework import serializers 
from .models import *

class usuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = 