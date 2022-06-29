from sqlite3 import apilevel
from tabnanny import verbose
from django import forms

class FamiliarFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)#, verbose='Nombre:')
    apellido = forms.CharField(max_length=30)#, verbose='Apellido:')
    edad = forms.IntegerField()#verbose='Edad:')
    fecha_nacimiento = forms.DateTimeField()#verbose='Fecha de Nacimiento:')
