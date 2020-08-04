from django.urls import path
from cliente.views import new_cliente, list_cliente, update_cliente, delete_cliente, detail_cliente


urlpatterns = [

    path('cliente_new', new_cliente, name='cliente_new'),
    path('', list_cliente, name='cliente_list'),
    path('cliente_update/<int:id>', update_cliente, name='cliente_update'),
    path('cliente_delete/<int:id>', delete_cliente, name='cliente_delete'),
    path('cliente_detail/<int:id>', detail_cliente, name='cliente_detail'),
]
