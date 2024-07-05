from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import usuarioSerializer, arteSerializer
from .models import Usuario, Arte
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    serializer = usuarioSerializer(instance=request.user)

    return Response(serializer.data, status=status.HTTP_200_OK)

#Arte

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def post_arte(request):
    serializer = arteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(artista=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_arte(request):
    artes = Arte.objects.all()
    serializer = ArteSerializer(artes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    