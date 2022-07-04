class Produto:

    def __init__(self, cod, nome, fabricante, quantidade = 0):
        self.cod = cod #input('Informe o código do produto:')
        self.nome = nome #input('Informe o nome do produto:')
        self.fabricante = fabricante #input('Informe o nome do fabricante:')
        self.quantidade = quantidade #input('Informe a quantidade de itens do produto:')

        print('\nObjeto salvo com eximea destreza mediante o sistema do estoque!\n')