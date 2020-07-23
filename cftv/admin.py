from django.contrib import admin
from .models import CftvOrcamento, Fabricante, Equipamentocftv, Cabo


class CftvOrcamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'ambiente', 'local')


class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class CaboAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'fabricante', 'aplicacao')


class EquipamentocftvAdmin(admin.ModelAdmin):
    list_display = ('equipamento_cftv', 'fabricante', 'modelo')


admin.site.register(CftvOrcamento, CftvOrcamentoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Cabo, CaboAdmin)
admin.site.register(Equipamentocftv, EquipamentocftvAdmin)
