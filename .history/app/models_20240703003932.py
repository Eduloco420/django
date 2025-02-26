from django.db import models

# Create your models here.

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    ap_pat = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    passWord = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)
    pfp = models.CharField(max_length=50)

class Arte(models.Model):
    artista = models.ForeignKey(usuario, on_delete=models.CASCADE)
    nom_arte = models.CharField(max_length=50)
    imagen_url = models.CharField(max_length=200)
    precio = models.IntegerField()
    desc = models.CharField(max_length=400)
    tec_usada = models.CharField(max_length=50)
    etiquetas = models.CharField(max_length=50)
    aprobado = models.BooleanField()
    vendido = models.BooleanField()
    
class venta(models.Model):
    

