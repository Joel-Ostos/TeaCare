
from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro_estudiante, name='registro_usuario'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('crear_materia/', views.crear_materia, name='crear_materia'),
    path('crear_profesor/', views.crear_profesor, name='crear_profesor'),
    path('perfil_estudiante/', views.perfil_usuario, name='perfil_usuario'),
    ]
