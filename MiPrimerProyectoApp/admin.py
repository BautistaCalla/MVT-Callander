from tabnanny import verbose
from django.contrib import admin

from .models import *

# Register your models here.

class FamiliarAdmin(admin.ModelAdmin):
    
   list_display = ('nombre', 'apellido', 'edad', 'fecha_nacimiento')
   search_fields = ('nombre', 'apellido', 'edad', 'fecha_nacimiento')
   

    
admin.site.register(Familiar)#, FamiliarAdmin)



