from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("favor ingresa un e-mail valido")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,**extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,**extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    mail = models.CharField(max_length=255 ,default='', blank = True, unique=True)
    
    nom = models.CharField(max_length=50, blank = True, null = True)
    ap_pat = models.CharField(max_length=50, blank = True, null = True)
    password = models.CharField(max_length=30)
    desc = models.CharField(max_length=400, blank = True, null = True)
    pfp = models.CharField(max_length=50, null= True)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mail'
    EMAIL_FIELD = 'mail'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def get_full_name(self):
        return self.name     

    def get_short_name(self):    
        return self.name or self.email.split('@')[0]

    


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
