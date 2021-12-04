from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=250, blank=True)
    edad = models.CharField(max_length=250, blank=True)
    carrera = models.CharField(max_length=250, blank=True)
    matricula = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name_plural = "alumnos"

    def __str__(self):
        return self.nombre