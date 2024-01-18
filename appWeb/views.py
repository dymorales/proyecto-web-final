from django.shortcuts import render
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Usuario, Noticia,CategoriaNoticia
from .models import contacto as Contacto
from .forms import clientForm, formularioUsuario, formularioContacto, formularioNoti
from django.db.models import Q



# Create your views here.
def registro(request):
    if request.method == "POST":
        nombres = request.POST["nombre"]
        correo = request.POST["email"]
        password = request.POST["password"]
        objCliente = Usuario.objects.create_user(
            nombre = nombres,
            email = correo,
            password = password,
            )
        objCliente.save()
        return  render(request,'home/home.html')
    else:    
        formu = formularioUsuario
        context = {
            'form' : formu
        }
        return render(request,'login/registro.html',context)

#Metodo Para logwea
def logueo(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['email']
        password1 = request.POST['password']
        user = authenticate(email=username, password=password1)
        if user is not None:
            login(request, user)
            return render(request,'home/home.html') #profile
        else:
            msg = 'Usuario Incorrecto!!'
            formu= clientForm
            context = {
                'form': formu,
                "msg": msg
            }
            return render(request, 'login/login.html', context)
    else:
        formu= clientForm
        context = {
            'form': formu
            }
        return render(request,'login/login.html', context)

def signout(request):
    logout(request)
    return redirect('/')


def home(request):
    return render(request, "Home/home.html")


def listaNoticia(request):
    if request.user.is_staff:
        noti = Noticia.objects.all()
        context = {
            "noticia": noti
        }
        return render (request,'noticia/lista_noticia.html', context)
    else: 
        noti = Noticia.objects.filter(aprobada=1)
        context = {
            "noticia": noti
        }
        return render (request,'noticia/lista_noticia.html', context)

def noticia(request, id_noticia):
    if request.user.is_staff:
        noti = Noticia.objects.filter(id_Noticia = id_noticia)
        context = {
            "noticia": noti
        }
        return render(request, "noticia/noticia_base.html", context)
    else:
        noti = Noticia.objects.filter(Q(id_Noticia = id_noticia) & Q(aprobada = 1))
        context = {
            "noticia": noti
        }
        return render(request, "noticia/noticia_base.html", context)

def aprobar(request, id_noticia):
    noti = Noticia.objects.get(id_Noticia = id_noticia)
    noti.aprobada = True
    noti.save()
    return redirect("/")

def buscar(request):
    query = request.GET.get('busca')
    if query:
        # Realizar la consulta a la base de datos SQLite utilizando el modelo Book
        if request.user.is_staff:
            results = Noticia.objects.filter(Q(titulo__icontains=query) | Q(autor__exact=query) | Q(id_Categoria__Descripcion = query.capitalize())).values("titulo","autor","id_Categoria__Descripcion", "id_Noticia","img" )
        else:
            results = Noticia.objects.filter(Q(titulo__icontains=query) & Q(aprobada = 1) | Q(autor__exact=query) & Q(aprobada = 1) | Q(id_Categoria__Descripcion = query.capitalize()) & Q(aprobada = 1)).values("titulo","autor","id_Categoria__Descripcion", "id_Noticia","img" )
    else:
        results = []
    return render(request, 'noticia/lista_noticia.html', {'query': query, 'noticia': results})

def creacion(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        autor = request.user
        detalle = request.POST["detalle"]
        contenido = request.POST["contenido"]
        fecha =request.POST["fecha"]
        ubicacion = request.POST["ubicacion"]
        img = request.POST["img"]
        cate = CategoriaNoticia.objects.get(id_categoria= request.POST["categoria"])

        noti = Noticia.objects.create(
            titulo = titulo,
            autor = autor,
            detalle = detalle,
            contenido = contenido,
            fecha =fecha,
            ubicacion = ubicacion,
            id_Categoria = cate,
            img = img
        )
        noti.save()
        return redirect ('/')
    else:
        formu = formularioNoti
        cate = CategoriaNoticia.objects.all()
        context = {
            "categoria": cate,
            "form": formu
        }
        return render(request,'Noticia/FormularioCreacion.html', context)

def rechazo(request):
    return render(request, 'Noticia/FormularioRechazo.html')

def contacto(request):
    if request.method=='POST':
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        tel = request.POST["telefono"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]
        contac = Contacto.objects.create(
            nombre = nombre,
            email = email,
            telefono = tel,
            asunto = asunto,
            mensaje = mensaje
        )
        contac.save()
        return redirect('/')
    else:
        form = formularioContacto
        context = {
            "formu": form
        }
        return render(request, "contacto/contacto.html", context)
    

def completo(request):
    contac = Contacto.objects.all()
    context = {
        "conacto" : contac
    }
    return render(request, "contacto/tabla.html", context)

def deportes(request):
    return render(request, "Noticia/deportes.html")
    
def messi(request):
    return render(request, "Noticia/messi.html")

def internacional(request):
    return render(request, "Noticia/internacional.html")
    
def espaiderman(request):
    return render(request, "Noticia/espaiderman.html")

def ministro(request):
    return render(request, "Noticia/ministro.html")

def salud(request):
    return render(request, "Noticia/salud.html")