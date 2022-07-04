from classe_Produto import *
from classe_Fabricante import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
        #self.listaProdutos.append(Produto(1, 'notbook', 'dell'))
        #self.listaProdutos.append(Produto(2, 'monitor', 'AOC'))


    def salvar_Produtos(self):
        if len(self.listaProdutos) > 0:
        #argumento2 = input('Informe o nome do produto:')
        #argumento3 = input('Informe o fabricante do produto:')
        #self.listaProdutos.append(Produto(cod=argumento1, nome=argumento2, fabricante=argumento3))
            self.mostrar_fabricantes()
            x = input('Insira o código do fabricante: ')
            print('Agora, insira os dados do produto.')
            for i in range(len(self.listaFabricantes)):
                if self.listaFabricantes[i].cod == x:
                    self.listaProdutos.append(Produto('0-' + str(len(self.listaProdutos) + 1), input('Nome: '),
                        self.listaFabricantes[i].nome_frabricante))
                    break
        else:
            print('O fabricante informado não possui parceria conosco!')

    def lista_Produtos_Codigo(self):
        for i in range(len(self.listaProdutos)):
             print('\n------------------------------------------------\n'
             'Código:', self.listaProdutos[i].cod, 
            'Nome:', self.listaProdutos[i].nome,
            'Fabricante:', self.listaProdutos[i].fabricante,
            'Quantidade em estoque:', self.listaProdutos[i].quantidade,
            '\n------------------------------------------------')

        resp = input('Digite o código do produto desejado:')
        
        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                print('Código:', self.listaProdutos[i].cod, 
            'Nome:', self.listaProdutos[i].nome,
            'Fabricante:', self.listaProdutos[i].fabricante,
            'Quantidade em estoque:', self.listaProdutos[i].quantidade)
            else:
                pass           

    def modificar_produto(self):
        resp = input('Digite o código do produto desejado:')

        for i in range(len(self.listaProdutos)):
            if resp == self.listaProdutos[i].cod:
                self.listaProdutos[i].nome= input('Digite o novo Nome do produto:')

    def listar_fabricantes(self):
        self.mostrar_fabricantes()

    def alterar_fabricantes(self):
        self.mostrar_fabricantes()
        in_cod = input('Insira o código do fabricante: ')
        for i in range(len(self.listaFabricantes)):
            if self.listaFabricantes[i].cod == in_cod:
                self.listaFabricantes[i].nome_frabricante = input('Insira aqui o novo nome.\n: ')
                print(self.listaFabricantes[i].nome_frabricante)

    def excluir_fabricantes(self):
        self.mostrar_fabricantes()
        in_cod = input('Insira o código do produto: ')
        for i in range(len(self.listaFabricantes)):
            if self.listaFabricantes[i].cod == in_cod:
                self.listaFabricantes.pop(i)
                print('Fabricante excluído com sucesso!!!')
                self.mostrar_fabricantes()
                break
            else:
                pass