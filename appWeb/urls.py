from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("login", views.logueo, name="login"),
    path('registro', views.registro, name="registro"),
    path('logout', views.signout, name="logout"),
    path('contacto', views.contacto, name="contacto"),

    path('noticia/<int:id_noticia>',views.noticia, name= "noticia"),
    path('LNoticia', views.listaNoticia, name="lista_noti"),
    path('aprobar/<int:id_noticia>', views.aprobar, name="aprobar"),

    path('creacion', views.creacion, name='Creacion'),
    path('rechazo',views.rechazo, name='rechazo'),

    path('buscar', views.buscar, name='buscar'),

    path('tabla', views.completo, name="tabla"),

]
