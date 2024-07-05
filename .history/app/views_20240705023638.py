from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import usuarioSerializer
from .models import Usuario
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):

    user = get_object_or_404(Usuario, email=request.data['email'])

    if not user.check_password(request.data['password']):
        return Response({"error": "Contraseña Incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
        
    token, created = Token.objects.get_or_create(user=user)
    serializer = usuarioSerializer(instance=user)
    
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def register(request):     
    serializer = usuarioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = Usuario.objects.get(email=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def profile(request):
    return Response({})