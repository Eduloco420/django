from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    ap_pat = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    passWord = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)
    pfp = models.CharField(max_length=50, null= True)
    admin = models.BooleanField()

class Arte(models.Model):
    artista = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nom_arte = models.CharField(max_length=50)
    imagen_url = models.CharField(max_length=200)
    precio = models.IntegerField()
    desc = models.CharField(max_length=400)
    tec_usada = models.CharField(max_length=50)
    etiquetas = models.CharField(max_length=50)
    aprobado = models.BooleanField()
    vendido = models.BooleanField()
