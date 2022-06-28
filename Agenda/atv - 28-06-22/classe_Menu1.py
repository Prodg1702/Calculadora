from classe_Estoque import *

class Menu:
    def __init__(self):
        estoque = Estoque()
        while True:
            entrada = input('\n1 - Novo Produto\n2 - Listar Produtos\n3 - Alterar Produto\n4 - Sair\n')
            if entrada == '1':
                estoque.salvar_Produtos()
            elif entrada == '2':
                estoque.lista_Produtos_Codigo()
            elif entrada == '3':
                estoque.modificar_produto()
            elif entrada == '4':
                break
            else:
                print('Não foi possível ajudar, entre em contato pelo 0800.')