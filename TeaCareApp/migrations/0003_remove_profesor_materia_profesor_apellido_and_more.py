# Generated by Django 4.2.7 on 2023-11-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeaCareApp', '0002_materia_estudiantes_materia_profesor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='materia',
        ),
        migrations.AddField(
            model_name='profesor',
            name='apellido',
            field=models.CharField(default='Apellido', max_length=100),
        ),
        migrations.AddField(
            model_name='profesor',
            name='correo',
            field=models.EmailField(default='correo', max_length=254),
        ),
        migrations.AddField(
            model_name='profesor',
            name='telefono',
            field=models.CharField(default='000', max_length=20),
        ),
    ]
