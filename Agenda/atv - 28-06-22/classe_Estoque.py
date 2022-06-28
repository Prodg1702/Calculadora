from classe_Produto import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []

    def salvar_Produtos(self):
        self.listaProdutos.append(Produto())

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
