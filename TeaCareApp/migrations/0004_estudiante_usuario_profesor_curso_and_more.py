# Generated by Django 4.2.7 on 2023-11-18 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TeaCareApp', '0003_remove_profesor_materia_profesor_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estudiante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profesor',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curso', to='TeaCareApp.curso'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='estudiantes', to='TeaCareApp.curso'),
        ),
    ]