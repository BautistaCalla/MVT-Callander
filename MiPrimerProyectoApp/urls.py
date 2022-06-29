
from django.urls import path

from .views import *

urlpatterns = [
 
    
    path('tablafamiliares/', tabla_familiares, name= 'familiares'),
    path('crear_familiar/', crear_familiar, name= 'crear-familiar'),
    path('buscar_familiar/', buscar_familiar, name='buscar-familiar'),
    path('eliminar_familiar/<familiar_id>', eliminar_familiar, name='eliminar-familiar'),
    path('editar_familiar/<familiar_id>',
         editar_familiar, name='editar-familiar'),

]


 