from django.db import models  #hereda del modelo base de django
from datetime import datetime

# Create your models here.
class Curso(models.Model): 
    curso_titulo = models.CharField(max_length=200)
    curso_contenido = models.TextField()
    curso_publicado = models.DateTimeField(
        "Fecha de publicacion", default=datetime.now()) #la hora y fecha actual por defecto

    def __str__(self):
        return self.curso_titulo

#el modelo se debe instalar en settings.py
#luego hacer las migraciones
#python manage.py makemigration
#python manage.py migrate