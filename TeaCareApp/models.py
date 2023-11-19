from django.db import models
from django.conf import settings

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    profesor = models.ForeignKey('Profesor', on_delete=models.SET_NULL, null=True, related_name='materias_dictadas')
    estudiantes = models.ManyToManyField('Estudiante', related_name='materias_inscritas')

    def __str__(self):
        return self.nombre
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Acudiente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Estudiante(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='estudiante')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    acudiente = models.ForeignKey(Acudiente, on_delete=models.CASCADE, related_name='estudiantes')
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True,related_name='estudiantes')
    materias = models.ManyToManyField('Materia', related_name='estudiantes_inscritos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, default='Apellido')
    correo = models.EmailField(default='correo')
    telefono = models.CharField(max_length=20, default='000')
    cursos = models.ManyToManyField(Curso, related_name='profesores')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True,related_name='curso')
    
    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.estudiante} - {self.materia}: {self.nota}"

class Mensaje(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje para {self.estudiante} - {self.fecha}"


