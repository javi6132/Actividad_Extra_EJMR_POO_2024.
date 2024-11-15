# admin.py
from django.contrib import admin
from .models import Libro

# Registrar el modelo Libro para que aparezca en el panel de administración
admin.site.register(Libro)
