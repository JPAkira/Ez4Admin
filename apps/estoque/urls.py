from django.urls import path
from apps.estoque import views

urlpatterns = [
    path('estoque', views.estoque, name='estoque'),
    path('estoque/cria_produto', views.cria_produto, name='cria_produto'),
    path('estoque/cria_produto_com_codigo', views.cria_produto_com_codigo, name='cria_produto_com_codigo'),
    path('estoque/adicionar_estoque_com_codigo', views.adicionar_estoque_com_codigo, name='adicionar_estoque_com_codigo'),
    path('estoque/deletar/<int:produto_codigo>', views.deletar_produto, name='deletar_produto'),
    path('estoque/editar_produto/<int:produto_codigo>', views.editar_produto, name='editar_produto'),
    path('estoque/editar_produto_com_codigo', views.editar_produto_com_codigo, name='editar_produto_com_codigo'),
    path('estoque/buscar', views.buscar, name='buscar_produto'),
]