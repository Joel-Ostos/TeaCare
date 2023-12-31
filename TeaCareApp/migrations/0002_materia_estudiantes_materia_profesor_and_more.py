# Generated by Django 4.2.7 on 2023-11-18 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeaCareApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='estudiantes',
            field=models.ManyToManyField(related_name='materias_inscritas', to='TeaCareApp.estudiante'),
        ),
        migrations.AddField(
            model_name='materia',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materias_dictadas', to='TeaCareApp.profesor'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='materias',
            field=models.ManyToManyField(related_name='estudiantes_inscritos', to='TeaCareApp.materia'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='materia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profesor_asignado', to='TeaCareApp.materia'),
        ),
    ]
