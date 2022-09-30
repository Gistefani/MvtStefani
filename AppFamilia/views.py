from django.shortcuts import render
from django.http import HttpResponse
from AppFamilia.models import Amigos
# Create your views here.

def inicio (request):
    return render (request, "inicio.html")

def familia (request):
    return render (request, "familia.html")    

def Amigos (request):
    if request.method == "POST":
        Amigos = Amigos(nombre = request.POST['nombre'], apellido = request.POST['apellido'], edad = request.POST['edad'])
        Amigos.save()
        return render(request, "familia.html")
    return render (request, "Amigos.html")  

def Asistencia (request):
    return render (request, "Asistencia.html")  