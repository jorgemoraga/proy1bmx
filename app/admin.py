from django.contrib import admin
from .models import Categoria, Bicicleta, Contacto
# Register your models here.

#incluimos los modelos en el dominio del admin
admin.site.register(Categoria)
admin.site.register(Bicicleta)
admin.site.register(Contacto)