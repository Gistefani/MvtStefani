from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Familia

def Home(request):
    return HttpResponse('Registro familiar')

def Familia(self):
    Familia = Familia(nombre="Miriam",apellido="Perez",edad="62",fechaNacimiento="23/6/1964",email="miristefani@gmail.com")
    Familia.save()

    documento= f'Familia: {Familia.nombre} {Familia.apellid} {Familia.edad} {Familia.fechaNacimiento} {Familia.email}'
    return HttpResponse(documento)
    