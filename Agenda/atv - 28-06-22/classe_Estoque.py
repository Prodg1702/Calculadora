from classe_Produto import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto(1, 'notbook', 'dell'))
        self.listaProdutos.append(Produto(2, 'monitor', 'AOC'))


    def salvar_Produtos(self):
        argumento1 = len(self.listaProdutos)+1
        argumento2 = input('Informe o nome do produto:')
        argumento3 = input('Informe o fabricante do produto:')
        self.listaProdutos.append(Produto(cod=argumento1, nome=argumento2, fabricante=argumento3))

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