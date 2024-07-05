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

        user = Usuario.objects.get(username=serializer.data['email'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})