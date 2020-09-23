from django.contrib import admin
from .models import Curso  #se debe registrar el modelo para que aparezca en el administrador
from tinymce.widgets import TinyMCE #importa el plugin tinymce
from django.db import models  #es necesario importar para poder haceerle un override

# Register your models here.

class CursoAdmin(admin.ModelAdmin):  #modifica la apariencia de nuestro modelo
    # fields = ("curso_publicado",
    #         "curso_contenido",
    #         "curso_titulo")  #se puede modificar el orden de los campos
    fieldsets = [  #fieldsets y fields no pueden declararse juntos
        ("Titulo/fecha", {"fields": ["curso_titulo", "curso_publicado"]}),
        ("Contenido", {"fields": ["curso_contenido"]})
    ] #agrupa en sets los campos

    formfield_overrides = {  #añade un widget para un tipo de campo
        models.TextField: {'widget':TinyMCE()}
    }

admin.site.register(Curso, CursoAdmin)  #esto resitra el modelo django le agregara una s al nombre del modelo