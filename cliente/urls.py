from django.urls import path
from cliente.views import new_cliente, list_cliente


urlpatterns = [

    path('cliente_new', new_cliente, name='cliente_new'),
    path('cliente_list', list_cliente, name='cliente_list'),
]
