from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import usuarioSerializer
from .models import Usuario
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def register(request):

    serializer = usuarioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    
        usuario = Usuario.objects.get(mail=serializer.data(['Usuario']))
        usuario.set_password(serializer.data['passWord'])
        user.save()

        token = Token.objects.Create(user=usuario)
        return Response({'token': token.key, 'user': serializer.date}, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def profile(request):
    return Response({})