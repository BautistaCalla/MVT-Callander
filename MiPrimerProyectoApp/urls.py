
from django.urls import path

from .views import *

urlpatterns = [
 
    
    path('familiares/', familiares, name= 'familiares'),
    path('crear_familiar/', crear_familiar, name= 'crear-familiar'),
    path('buscar_familiar/', buscar_familiar, name='buscar-familiar'),
    path('eliminar_familiar/<familiar_id>', eliminar_familiar, name='eliminar-familiar'),
    path('editar_familiar/<familiar_id>',
         editar_familiar, name='editar-familiar'),
    
    path('familiares/list', FamiliarList.as_view(), name='familiares_list'),
    path(r'^(?P<pk>\d+)$', FamiliarDetail.as_view(), name='familiares_detail'),
    path(r'^nuevo$', FamiliarCreate.as_view(), name='familiares_create'),
    path(r'^editar/(?P<pk>\d+)$', FamiliarUpdate.as_view(), name='familiares_update'),
    path(r'^eliminar(?P<pk>\d+)$', FamiliarDelete.as_view(), name='familiares_delate'),

]


 