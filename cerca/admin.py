from django.contrib import admin
from .models import CercaOrcamento, Equipamentocerca


class CercaOrcamentoAdmin(admin.ModelAdmin):
    list_display = ('perimetro', 'elevacao')


class EquipamentocercaAdmin(admin.ModelAdmin):
    list_display = ('equipamento_cerca', 'fabricante', )


admin.site.register(CercaOrcamento, CercaOrcamentoAdmin)
admin.site.register(Equipamentocerca, EquipamentocercaAdmin)