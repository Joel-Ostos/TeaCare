from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Colegio, Acudiente, Estudiante, Materia, Curso, Profesor

class RegistroEstudianteForm(forms.ModelForm):
    nombre_usuario = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    codigo_colegio = forms.CharField(max_length=50)
    acudiente_nombre = forms.CharField(max_length=100)
    acudiente_apellido = forms.CharField(max_length=100)
    acudiente_correo = forms.EmailField()
    acudiente_telefono = forms.CharField(max_length=20)
    materias = forms.ModelMultipleChoiceField(queryset=Materia.objects.all(), required=False)

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'edad', 'curso']

    def clean_codigo_colegio(self):
        codigo = self.cleaned_data['codigo_colegio']
        if not Colegio.objects.filter(codigo=codigo).exists():
            raise forms.ValidationError("El código del colegio no es válido.")
        return codigo

    def save(self, commit=True):
        usuario = User.objects.create_user(
                username=self.cleaned_data['nombre_usuario'],
                email=self.cleaned_data['correo'],
                password=self.cleaned_data['password']
                )
        acudiente, _ = Acudiente.objects.get_or_create(
                nombre=self.cleaned_data['acudiente_nombre'],
                apellido=self.cleaned_data['acudiente_apellido'],
                defaults={
                    'correo': self.cleaned_data['acudiente_correo'],
                    'telefono': self.cleaned_data['acudiente_telefono']
                    }
                )
        estudiante = super().save(commit=False)
        estudiante.usuario = usuario
        estudiante.acudiente = acudiente
        if commit:
            estudiante.save()
        return estudiante
class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'colegio', 'profesor', 'estudiantes']

    def __init__(self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields['estudiantes'].required = False

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'colegio']


class SeleccionRolForm(forms.Form):
    ROLES = (
        ('acudiente', 'Acudiente'),
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    )
    rol = forms.ChoiceField(choices=ROLES, label='Seleccione su rol')

class RegistroAcudienteForm(forms.ModelForm):
    class Meta:
        model = Acudiente
        fields = ['nombre', 'apellido', 'correo', 'telefono']

class RegistroProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'curso']

    def clean_correo(self):
        correo = self.cleaned_data['correo']
        if Profesor.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Un profesor con este correo ya está registrado.")
        return correo

