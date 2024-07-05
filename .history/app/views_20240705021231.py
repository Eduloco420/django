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
    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})