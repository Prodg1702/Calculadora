from classe_Estoque import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()

    def compra(self):
        entrada = input('Código do produto:')
        for i in range(len(self.entrada.listaProdutos)):
            if  entrada == self.entrada.listaProdutos[i].cod:
                self.entrada.listaProdutos[i].quantidade = input('Quantidade comprada:')
