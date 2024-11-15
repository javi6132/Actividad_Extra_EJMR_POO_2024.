# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

# Vista para listar todos los libros
def listar_libros(request):
    libros = Libro.objects.all()  # Obtiene todos los libros de la base de datos
    return render(request, 'pages/listar.html', {'libros': libros})

# Vista para crear un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo libro en la base de datos
            return redirect('libros:listar')  # Redirige al listado de libros
    else:
        form = LibroForm()
    
    return render(request, 'pages/formulario.html', {'form': form})

# Vista para editar un libro existente
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)  # Obtiene el libro por su ID
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)  # Pasa la instancia para editar
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('libros:listar')  # Redirige al listado de libros
    else:
        form = LibroForm(instance=libro)
    
    return render(request, 'pages/formulario.html', {'form': form, 'libro': libro})

# Vista para eliminar un libro
def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)  # Obtiene el libro por su ID
    if request.method == 'POST':
        libro.delete()  # Elimina el libro
        return redirect('libros:listar')  # Redirige al listado de libros
    return render(request, 'pages/eliminar.html', {'libro': libro})
