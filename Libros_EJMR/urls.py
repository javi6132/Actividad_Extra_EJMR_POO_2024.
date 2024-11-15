# Libros_EJMR/urls.py
from django.urls import path
from . import views

app_name = 'libros'  # Define el espacio de nombres para la aplicación

urlpatterns = [
    path('', views.listar_libros, name='listar'),  # Redirige 'libros/' a la vista listar_libros
    path('listar/', views.listar_libros, name='listar'),  # Listar libros
    path('crear/', views.crear_libro, name='crear'),  # Crear libro
    path('editar/<int:id>/', views.editar_libro, name='editar'),  # Editar libro
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar'),  # Eliminar libro
]
