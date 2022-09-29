from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio (request):
    return render (request, "inicio.html")

def familia (request):
    return render (request, "familia.html")    

def Amigos (request):
    return render (request, "Amigos.html")  

def Asistencia (request):
    return render (request, "Asistencia.html")  