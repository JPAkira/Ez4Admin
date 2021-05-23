from django.urls import path
from apps.clientes import views

urlpatterns = [
    path('clientes', views.clientes, name='clientes'),
    path('clientes/cria', views.cria_cliente, name='cria_cliente'),
    path('clientes/deleta/<int:cliente_id>', views.deleta_cliente, name='deletar_cliente'),
    path('clientes/editar/<int:cliente_id>', views.editar_cliente, name='editar_cliente'),
    path('atualizar_cliente', views.atualizar_cliente, name='atualizar_cliente'),
    path('clientes/buscar', views.buscar, name='buscar'),
]