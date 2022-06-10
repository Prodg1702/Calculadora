from tkinter import * 

def validar():
    valida = False

    #pega o dia
    dia = (int(in2_fr1.get()[:2]))

    #pega o mes
    mes = (int(in2_fr1.get()[3:4]))
    if mes == 0:
        mes = (int(in2_fr1.get()[3:5]))

    #pega o ano
    ano = (int(in2_fr1.get()[6:10]))

    # Meses com 31 dias
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if (dia <= 31):
            valida = True
    # Meses com 30 dias
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if (dia <= 30):
            valida = True
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if (dia <= 29):
                valida = True
        elif (dia <= 28):
            valida = True

    if (valida):
        lb12_fr3['text'] = "Data válida"
    else:
       lb12_fr3['text'] = "Data inválida"

def capitura(event=None):
    x=in2_fr1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in2_fr1.delete(0, 'end')
    in2_fr1.insert(0, y)



#criando janela
root = Tk()
root.title('Cadastro')
root.geometry('1020x230+720+350')
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)
root.grid_rowconfigure(8, weight=1)
root.grid_rowconfigure(9, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)
root.grid_columnconfigure(7, weight=1)
root.grid_columnconfigure(8, weight=1)
root.grid_columnconfigure(9, weight=1)
root.grid_columnconfigure(10, weight=1)


fr1 = LabelFrame(root, text='Dados Pessoais', background='#ededed')
fr2 = LabelFrame(root, text='Endereço', background='#ededed')
fr3 = Frame(root, background='#ededed')

#criando widgets dados pessoais
lb1_fr1 = Label(fr1, text='Dados Pessoais', font='Arial 20', fg='cyan')
lb2_fr1 = Label(fr1, text='Nome:', font='Arial 16')
in1_fr1 = Entry(fr1, font='Arial 16')
lb3_fr1 = Label(fr1, text='Data Nasc:', font='Arial 16')
in2_fr1 = Entry(fr1, text='', font='Arial 16',)
in2_fr1.bind('<KeyRelease>', capitura)
lb4_fr1 = Label(fr1, text='CPF:', font='Arial 16')
in3_fr1 = Entry(fr1, font='Arial 16')
lb5_fr1 = Label(fr1, text='Telefone', font='Arial 16')
in4_fr1 = Entry(fr1, font='Arial 16')


#criando widgets endereço
lb6_fr2 = Label(fr2, text='Endereço', font='Arial 20', fg='cyan')
lb7_fr2 = Label(fr2, text='Rua:', font='Arial 16')
in5_fr2 = Entry(fr2, font='Arial 16')
lb8_fr2 = Label(fr2, text='Bairro:', font='Arial 16')
in6_fr2 = Entry(fr2, font='Arial 16')
lb9_fr2 = Label(fr2, text='Cidade:', font='Arial 16')
in7_fr2 = Entry(fr2, font='Arial 16')
lb10_fr2 = Label(fr2, text='N°', font='Arial 16')
in8_fr2 = Entry(fr2, font='Arial 16')
lb11_fr2 = Label(fr2, text='UF', font='Arial 16')
in9_fr2 = Entry(fr2, font='Arial 16')


#Botões
bt1_fr3 = Button(fr3, text='Gravar Dados', font='Arial 12', command=validar)
bt2_fr3 = Button(fr3, text='Listar Dados', font='Arial 12')
lb12_fr3 = Label(fr3, text='', font='Arial 16')



#frames
fr1.grid(sticky=W, padx= 15)
fr2.grid(sticky=W, padx= 15)
fr3.grid(sticky=W, padx= 15, pady= 15)


#organizando widgets
#dados pessoais/nome
lb2_fr1.grid(row= 1, column= 0,sticky=NE, pady= 2)
in1_fr1.grid(row= 1, column= 1,columnspan= 6, sticky=NSEW, pady= 2)

#Data nascimento
lb3_fr1.grid(row= 2, column= 0)
in2_fr1.grid(row= 2, column= 1)

#CPF
lb4_fr1.grid(row= 2, column= 3,sticky=NE)
in3_fr1.grid(row= 2, column= 4)

#Telefone
lb5_fr1.grid(row= 2, column= 5)
in4_fr1.grid(row= 2, column= 6)

#Endereço/rua
lb7_fr2.grid(row= 1, column= 0, sticky=NE, pady= 2)
in5_fr2.grid(row= 1, column= 1, columnspan=4, sticky=NSEW, pady= 2)

#bairro
lb8_fr2.grid(row= 2, column= 0, sticky=NE)
in6_fr2.grid(row= 2, column= 1, sticky=NSEW)

#cidade
lb9_fr2.grid(row= 2, column= 2, sticky=NSEW)
in7_fr2.grid(row= 2, column= 3, sticky=NSEW)

#n°
lb10_fr2.grid(row= 1, column= 4, sticky=NSEW, pady= 2)
in8_fr2.grid(row= 1, column= 5, sticky=NSEW, pady= 2)

#UF
lb11_fr2.grid(row=2, column= 4, sticky=NSEW)
in9_fr2.grid(row= 2, column= 5, sticky=NSEW)

#Botão
bt1_fr3.grid(row=0, column=0)
bt2_fr3.grid(row=0, column=1)
lb12_fr3.grid(row=0, column=3)

#executar e manter janela aberta
root.mainloop()