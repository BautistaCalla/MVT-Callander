import datetime
from sqlite3 import Cursor 

from django.shortcuts import redirect, render
from django.http import HttpResponse
from MiPrimerProyectoApp.apps import MiprimerproyectoappConfig

from MiPrimerProyectoApp.models import * 
from .forms import FamiliarFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout




def login_request(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request=request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return redirect('login')
        else:
            return redirect('login')   
            
    form = AuthenticationForm()

    return render(request, 'MiPrimerProyectoApp/login.html', {'form': form})

def register_request(request):
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') #es la primer contraseña no la confirmacion
            
            form.save() # registramos el usuario
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
            return redirect('login')
        
        return render(request, 'MiPrimerProyectoApp/register.html', {'form': form})
    
    form = UserCreationForm()
    
    return render(request, 'MiPrimerProyectoApp/register.html', {'form' : form})

def crear_familiar(request):
    
    if request.method == 'POST':
        
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():
            
            info_familiar = formulario.cleaned_data
        
            familiar = Familiar(nombre=info_familiar['nombre'],
                                apellido=info_familiar['apellido'],
                                edad=info_familiar['edad'],
                                fecha_nacimiento=info_familiar['fecha_nacimiento'])
            familiar.save()
        
            return redirect('familiares')
        
        else:
            
            return render(request, 'MiPrimerProyectoApp/formulario_familiar.html', {'form': formulario})
        
    else:
        
        formularioVacio = FamiliarFormulario()
        
        return render(request, 'MiPrimerProyectoApp/formulario_familiar.html', {'form':formularioVacio})
    
def eliminar_familiar(request, familiar_id):
    
    familiar = Familiar.objects.get(id=familiar_id)
    familiar.delete()
    
    return redirect('familiares')


def editar_familiar(request, familiar_id):

    familiar = Familiar.objects.get(id=familiar_id)
    
    if request.method == 'POST':
        
        formulario = FamiliarFormulario(request.POST)
        
        if formulario.is_valid():
                
            info_familiar = formulario.cleaned_data
                
            familiar.nombre=info_familiar['nombre']
            familiar.apellido=info_familiar['apellido']
            familiar.edad=info_familiar['edad']
            familiar.fecha_nacimiento=info_familiar['fecha_nacimiento']
            familiar.save()
            
            return redirect('familiares')
    
    formulario = FamiliarFormulario(initial={'nombre': familiar.nombre, 'apellido': familiar.apellido,
                               'edad': familiar.edad, 'fecha_nacimiento': familiar.fecha_nacimiento})

    return render(request, 'MiPrimerProyectoApp/formulario_familiar.html', {'form': formulario})


def buscar_familiar(request):
    if request.method == 'POST':
        
        familiar = request.POST['Nombre']
        
        familiares = Familiar.objects.filter(nombre__icontains=familiar)
        
        return render(request, 'MiPrimerProyectoApp/busqueda_familiar.html', {'familiares': familiares})
    
    else:   
        
        familiares = []
    
        return render(request, 'MiPrimerProyectoApp/busqueda_familiar.html', {'familiares': familiares})

def familiares(request):
    
    data = Familiar.objects.all()
    
    return render(request, 'MiPrimerProyectoApp/familiares.html', {'data': data})

class FamiliarList(ListView):
    
    model = Familiar
    template_name = 'MiPrimerProyectoApp/familiares_list.html'
    

class FamiliarDetail(DetailView):
    
    model = Familiar
    template_name = 'MiPrimerProyectoApp/familiares_detail.html'
    
class FamiliarCreate(CreateView):
    
    model = Familiar
    success_url = '/coderapp/familiares/list'
    fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']
    

class FamiliarUpdate(UpdateView):

    model = Familiar
    success_url = '/coderapp/familiares/list'
    fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']
    

class FamiliarDelete(DeleteView):

    model = Familiar
    success_url = '/coderapp/familiares/list'
    fields = ['nombre', 'apellido', 'edad', 'fecha_nacimiento']


def inicio(request):

    data = Familiar.objects.all()

    return render(request, 'MiPrimerProyectoApp/index.html', {'data': data})


def base(request):

    return render(request, 'MiPrimerProyectoApp/base.html', {})

