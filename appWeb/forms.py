from django.forms import ModelForm , TextInput, Textarea, ClearableFileInput
from . import models
from django import forms

class clientForm (ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["email","password"]
        widgets= {
            'email' :  TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico'}),
            'password' :  TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'type':'password'})
        }

class formularioUsuario(ModelForm):
    class Meta:
        model = models.Usuario
        fields= ["password","email", "nombre"]
        widgets = {
            'email' :  TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electronico', "id":"idCorreo","name":"Correo"}),
            "nombre": TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo', "id": "idNombre","name":"Nombre"}),
            "password" : TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña', "id" : "idContra", "type" : "password","name":"Password"})
        }

class formularioContacto(ModelForm):
    class Meta:
        model = models.contacto
        fields = ["nombre","email","telefono", "asunto", "mensaje"]
        widgets = {
            "nombre" : TextInput(attrs={"class":"input" , "type": "text" , "id":"asunto", "required": "True", "placeholder" : "Inrgese Nombre"}),
            "email" : TextInput(attrs={"class":"input" , "type": "email" , "id":"asunto", "required": "True", "placeholder" : "Inrgese Correo"}),
            "telefono" : TextInput(attrs={"class":"input" , "type": "number" , "id":"asunto", "required": "True", "placeholder" : "Inrgese Telefono"}),
            "asunto" : TextInput(attrs={"class":"input" , "type": "text" , "id":"asunto", "required": "True", "placeholder" : "Inrgese Asunto"}),
            "mensaje" : Textarea(attrs={"class":"input" , "type": "textarea" , "id":"asunto", "required": "True", "placeholder" : "Inrgese Mensaje"})
            
        }

class formularioNoti(ModelForm):
    class Meta:
        model = models.Noticia
        fields=["titulo","detalle", "contenido", "autor", "fecha","ubicacion", "img"]
        widgets = {
            "titulo" : TextInput(attrs={"class":"input", "type" : "text",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese Titulo"}),
            "detalle" : TextInput(attrs={"class":"input", "type" : "text",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese detalle"}),
            "contenido" : Textarea(attrs={"class":"input", "type" : "text",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese contenido"}),
            "autor" : TextInput(attrs={"class":"input", "type" : "text",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese autor"}),
            "fecha" : TextInput(attrs={"class":"input", "type" : "date",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese fecha"}),
            "ubicacion" : TextInput(attrs={"class":"input", "type" : "text",  "id" : "nombre", "required": "True", "placeholder" : "Ingrese Ubicacion"}),
            "img" : ClearableFileInput(attrs={"class": "input", "type": "file", "id": "nombre", "required": "True", "name" : "img"})
        }
