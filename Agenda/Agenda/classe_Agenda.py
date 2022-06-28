from classe_Contato import *

class Agenda:
    def __init__(self):
        self.listaContatos = []

    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Cod: ',self.listaContatos[i].cod, 
            ' Nome: ', self.listaContatos[i].nome, 
            ' Telefone: ',self.listaContatos[1].telefone)

    def modificar_telefone(self, argumento1, argumento2):
        controle = argumento1
        for i in range(len(self.listaContatos)):
            if controle == self.listaContatos[i].cod:
                self.telefone = argumento2