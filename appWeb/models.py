
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.utils.timezone import now
# Create your models here

class usuarioManager (BaseUserManager):
    def create_user(self,email,nombre, password = None):
        if not email:
            raise ValueError('El usuario no tiene correo!')
        cliente = self.model(email = self.normalize_email(email),
                            nombre = nombre)
        cliente.set_password(password)
        cliente.save()
        return cliente
    
    def create_superuser(self,email,nombre, password):
        cliente= self.create_user(email, nombre = nombre,
                                    password=password)
        cliente.id_TipoUsuario=True
        cliente.is_admin = True
        cliente.save()
        return cliente
    

class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=40, primary_key=True)
    password = models.CharField(max_length=100, null=False, default="")
    email = models.CharField(unique=True, max_length=40, default="")
    TipoUsuario = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = usuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
            return self.is_admin
    
    def __str__(self):
        return str(self.nombre)


class CategoriaNoticia(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return str(self.Descripcion)

class Noticia(models.Model):
    id_Noticia = models.AutoField(db_column='id_Noticia',primary_key=True)
    titulo = models.CharField(max_length=500)
    detalle = models.CharField(max_length=4000)
    contenido = models.CharField(blank=True, max_length=10000)
    autor = models.ForeignKey('Usuario',on_delete=models.CASCADE,db_column='Nombre')
    fecha = models.DateField(blank=True,default=now, null=True)
    ubicacion = models.CharField(max_length=40)
    img = models.ImageField(upload_to="img/")
    id_Categoria = models.ForeignKey('CategoriaNoticia',on_delete=models.CASCADE,db_column='Descripcion', default="")
    aprobada = models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.titulo)
    
class contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    email = models.CharField(max_length=100)
    telefono = models.IntegerField()
    asunto = models.CharField(max_length=3000)
    mensaje = models.TextField()

    def __str__(self):
        return (f'El usuario con correo {self.email} se contacta por {self.asunto}')