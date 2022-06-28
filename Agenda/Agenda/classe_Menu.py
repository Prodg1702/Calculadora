from classe_Agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()

        #entrada = input('1 - Novo Contato\n2 - Listar Contatos\n0 - Sair')

        while True:
            entrada = input('1 - Novo Contato\n2 - Listar Contatos\n3 - Modificar Contato\n0 -Sair\n')
            if entrada == '1':
                agenda.salvar_contatos()
            elif entrada == '2':
                agenda.listar_contatos()
            elif entrada == '3':
                entrada1 = input('Informe o codigo do contato que deseja modificar:')
                entrada2 = input('Digite o novo telefone:')
                agenda.modificar_telefone(argumento1, argumento2)
            elif entrada == '0':
                break
            else:
                print('Erro crítico, a maquina entrará em modo destruição')