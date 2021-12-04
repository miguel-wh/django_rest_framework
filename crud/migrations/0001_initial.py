# Generated by Django 3.2.9 on 2021-12-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(blank=True, max_length=250)),
                ('edad', models.CharField(blank=True, max_length=250)),
                ('carrera', models.CharField(blank=True, max_length=250)),
                ('matricula', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'alumnos',
            },
        ),
    ]
