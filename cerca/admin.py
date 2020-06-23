from django.contrib import admin
from .models import CercaOrcamento


class CercaOrcamentoAdmin(admin.ModelAdmin):
    list_display = ('perimetro', 'elevacao')


admin.site.register(CercaOrcamento, CercaOrcamentoAdmin)
