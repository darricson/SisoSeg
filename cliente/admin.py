from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'telefone')


admin.site.register(Cliente, ClienteAdmin)
