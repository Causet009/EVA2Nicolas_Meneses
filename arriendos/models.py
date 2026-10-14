from django.db import models


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    valor_diario = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Arriendo(models.Model):
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE,
        related_name='arriendos'
    )
    cliente = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    dias = models.PositiveIntegerField()
    valor_total = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cliente} - {self.equipo.nombre}"