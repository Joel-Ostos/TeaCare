from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroEstudianteForm
from .forms import RegistroProfesorForm
from .models import Colegio, Acudiente, Estudiante, Profesor
from .forms import CursoForm
from .forms import MateriaForm

def verificar_codigo_colegio(request):
    if request.method == 'POST':
        form = SeleccionRolForm(request.POST)
        if form.is_valid():
            codigo_colegio = form.cleaned_data['codigo_colegio']
            rol_seleccionado = form.cleaned_data['rol']

            if not Colegio.objects.filter(codigo=codigo_colegio).exists():
                return render(request, 'seleccion_rol.html', {'form': form, 'error': 'Código de colegio inválido.'})

            # Redirigir al formulario correspondiente
            if rol_seleccionado == 'acudiente':
                return redirect('registro_acudiente')
            elif rol_seleccionado == 'profesor':
                return redirect('registro_profesor')
            else: # estudiante
                return redirect('registro_estudiante')
    else:
        form = SeleccionRolForm()
    return render(request, 'seleccion_rol.html', {'form': form})

def registro_estudiante(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            nombre_estudiante = form.cleaned_data['nombre']
            apellido_estudiante = form.cleaned_data['apellido']

            # Comprobar si ya existe un estudiante con el mismo nombre y apellido
            if Estudiante.objects.filter(nombre=nombre_estudiante, apellido=apellido_estudiante).exists():
                messages.error(request, 'El estudiante ya se creó antes.')
                return render(request, 'estudiante/registro_estudiante.html', {'form': form})

            # Crear Acudiente
            nombre_acudiente = form.cleaned_data['acudiente_nombre']
            apellido_acudiente = form.cleaned_data['acudiente_apellido']
            correo_acudiente = form.cleaned_data['acudiente_correo']
            telefono_acudiente = form.cleaned_data['acudiente_telefono']

            acudiente, created = Acudiente.objects.get_or_create(
                nombre=nombre_acudiente, 
                apellido=apellido_acudiente, 
                defaults={'correo': correo_acudiente, 'telefono': telefono_acudiente}
            )

            estudiante = form.save(commit=False)
            estudiante.acudiente = acudiente
            estudiante.save()

            return render(request, 'estudiante/perfil_estudiante.html', {'form': form})
        else:
            return render(request, 'estudiante/registro_estudiante.html', {'form': form})
    else:
        form = RegistroEstudianteForm()
        return render(request, 'estudiante/registro_estudiante.html', {'form': form})

def crear_materia(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            materia = form.save()
            return redirect('vista_despues_creacion')
    else:
        form = MateriaForm()
        return render(request, 'crear_materia.html', {'form': form})

# En tu archivo views.py

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguna_vista_post_creacion')
    else:
        form = CursoForm()
        return render(request, 'crear_curso.html', {'form': form})

def seleccion_rol(request):
    if request.method == 'POST':
        form = SeleccionRolForm(request.POST)
        if form.is_valid():
            rol_seleccionado = form.cleaned_data['rol']
            return redirect(f'registro_{rol_seleccionado}')
    else:
        form = SeleccionRolForm()
    return render(request, 'seleccion_rol.html', {'form': form})

def crear_profesor(request):
    if request.method == 'POST':
        form = RegistroProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alguna_url_despues_registro')  # Reemplaza con la URL adecuada
    else:
        form = RegistroProfesorForm()
    return render(request, 'registro_profesor.html', {'form': form})

from django.shortcuts import render
from .models import Estudiante, Curso, Materia  # Asegúrate de importar los modelos necesarios

def perfil_usuario(request):
    usuario = request.user
    estudiante = Estudiante.objects.get(usuario=usuario)
    edad = estudiante.edad
    curso = estudiante.curso
    telefono = estudiante.telefono
    correo = estudiante.correo
    acudiente = estudiante.acudiente
    materias = estudiante.materias.all()

    return render(request, 'perfil_usuario.html', {
        'usuario': usuario,
        'estudiante': estudiante,
        'edad': edad,
        'acudiente' : acudiente,
        'telefono': telefono,
        'correo': correo,
        'curso': curso,
        'materias': materias,
    })

