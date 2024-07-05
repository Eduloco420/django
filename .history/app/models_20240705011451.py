from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=50)
    ap_pat = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    passWord = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)
    pfp = models.CharField(max_length=50, null= True)
    admin = models.BooleanField(default=False)
    last_login = models.DateField(default='1900-01-01')

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['nombre', 'ap_pat']

    def __str__(self):
        return self.mail

    @property
    def is_staff(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin


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
