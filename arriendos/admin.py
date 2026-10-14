from django.contrib import admin
from .models import Equipo, Arriendo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'marca',
        'tipo',
        'valor_diario_formateado',
        'disponible',
    )

    list_filter = (
        'tipo',
        'disponible',
    )

    search_fields = (
        'nombre',
        'marca',
        'tipo',
    )

    @admin.display(
        description='Valor diario',
        ordering='valor_diario'
    )
    def valor_diario_formateado(self, obj):
        return f"${obj.valor_diario:,}".replace(",", ".")


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'equipo',
        'fecha_inicio',
        'dias',
        'valor_total_formateado',
        'activo',
    )

    list_filter = (
        'activo',
        'fecha_inicio',
    )

    search_fields = (
        'cliente',
        'equipo__nombre',
    )

    @admin.display(
        description='Valor total',
        ordering='valor_total'
    )
    def valor_total_formateado(self, obj):
        return f"${obj.valor_total:,}".replace(",", ".")