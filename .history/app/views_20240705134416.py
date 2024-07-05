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
    serializer = arteSerializer(artes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_arte(request,arte_id):
    try:
        arte = Arte.objects.get(id=arte_id)
    except Arte.DoesNotExist:
        return Response({'error': 'Arte no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    arte.delete()
    return Response({'message': 'Arte eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_arte(request, arte_id):
    print(request.user.is_staff)
    try:
        arte = Arte.objects.get(id=arte_id)
    except Arte.DoesNotExist:
        return Response({'error': 'Arte no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    if request.user != arte.artista:
        return Response({'error': 'No tienes permiso para editar este arte'}, status=status.HTTP_403_FORBIDDEN)

    serializer = ArteSerializer(arte, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)