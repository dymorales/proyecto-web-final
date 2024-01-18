from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Noticia)
admin.site.register(models.CategoriaNoticia)
admin.site.register(models.Usuario)
admin.site.register(models.contacto)