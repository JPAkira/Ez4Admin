from django.urls import path
from apps.vendas import views

urlpatterns = [
    path('vendas', views.vendas, name='vendas'),
    path('vendas/cria_venda/<int:cliente_id>', views.cria_venda, name='cria_venda'),
    path('vendas/selecionar_cliente', views.selecionar_cliente, name='selecionar_cliente'),
    path('vendas/adicionar_produto/<int:venda_id>', views.adicionar_produto, name='adicionar_produto'),
    path('vendas/salvar_produto', views.salvar_produto, name='salvar_produto'),
    path('vendas/salvar_venda/<int:cliente_id>', views.salvar_venda, name='salvar_venda'),
    path('vendas/deleta_venda/<int:venda_id>', views.deleta_venda, name='deleta_venda'),
    path('vendas/finalizar_venda/<int:venda_id>', views.finalizar_venda, name='finalizar_venda'),
    path('vendas/salvar_produto/deletar_produto_venda/<int:produto_id>', views.deletar_produto_venda, name='deletar_produto_venda'),
    path('vendas/buscar', views.busca_venda, name='busca_venda'),
    path('vendas/busca_cliente_venda', views.busca_cliente_venda, name='busca_cliente_venda'),
]