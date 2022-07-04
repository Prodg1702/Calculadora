from classe_Estoque import*
from classe_Historico import*

class Compras:
    def __init__(self):
        self.entrada = Estoque()
        self.historico = Historico()
    def comprar(self):
        entrada = input('Informe o código do Produto:  ')
        for i in range(len(self.entrada.listaProdutos)):
            if entrada == self.entrada.listaProdutos[i].cod:
                x=int(input('Quantos deseja comprar?  '))
                self.entrada.listaProdutos[i].quantidade += int(x)
                self.historico.transacoes.append(f'Compra de {x} unidades do produto: {self.entrada.listaProdutos[i].nome}')
                break
    def extrato(self):
        print(self.historico.compras_vendas())