import datetime 

from django.shortcuts import render
from django.http import HttpResponse
from MiPrimerProyectoApp.models import *

def crear_familiar(request):
    
    nombre='Maria'
    apellido='Acosta'
    edad=40
    fecha_nacimiento = datetime.date(1982, 10, 19)
    
    familiar = Familiar(nombre=nombre,
                        apellido=apellido,
                        edad=edad,
                        fecha_nacimiento=fecha_nacimiento)
    familiar.save()

    return HttpResponse(f'Hemos agregado el familiar {nombre} {apellido}')


def tabla_familiares(request):
    
    data = Familiar.objects.all()
    
    return render(request, 'MiPrimerProyectoApp/familiares.html', {'data': data})
