import imp
from classe_Estoque import *
from classe_Compra import *
from classe_Venda import *

class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compras
        venda = Vendas()
        compra.entrada = estoque
        venda.entrada = estoque
        while True:
            entrada = input('\n1 - Novo Produto\n2 - Listar Produtos\n3 - Alterar Produto\n4 - Listar Fabricantes\n5 - Cadastrar Fabricante\n6 - Excluir Fabricante\n7 - Comprar\n8 - Vendas\n9 - Sair')

            if entrada == '1':
                estoque.salvar_Produtos()
            elif entrada == '2':
                estoque.lista_Produtos_Codigo()
            elif entrada == '3':
                estoque.modificar_produto()
            elif entrada == '4':
                estoque.listar_fabricantes()
            elif entrada == '5':
                estoque.salvar_fabricantes() 
            elif entrada == '6':
                estoque.excluir_fabricantes()
            elif entrada == '7':
                break
            else:
                print('Não foi possível ajudar, entre em contato pelo 0800.')
