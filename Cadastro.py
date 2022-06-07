from tkinter import * 

#criando janela
root = Tk()
root.geometry('980x315+720+350')
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


fr1 = Frame(root, background='#ededed')
fr2 = Frame(root, background='#ededed')
fr3 = Frame(root, background='#ededed')

#criando widgets dados pessoais
lb1_fr1 = Label(fr1, text='Dados Pessoais', font='Arial 20', fg='cyan')
lb2_fr1 = Label(fr1, text='Nome:', font='Arial 16')
in1_fr1 = Entry(fr1, font='Arial 16')
lb3_fr1 = Label(fr1, text='Data Nasc:', font='Arial 16')
in2_fr1 = Entry(fr1, font='Arial 16')
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
bt1_fr3 = Button(fr3, text='Gravar Dados', font='Arial 12')
bt2_fr3 = Button(fr3, text='Listar Dados', font='Arial 12')



#frames
fr1.grid(sticky=W)
fr2.grid()
fr3.grid(sticky=W, pady= 15)


#organizando widgets
#dados pessoais/nome
lb1_fr1.grid(row= 0, column= 0,)
lb2_fr1.grid(row= 1, column= 0,sticky=NE)
in1_fr1.grid(row= 1, column= 1,columnspan= 2, sticky=NE)

#Data nascimento
lb3_fr1.grid(row= 2, column= 0,sticky=NE)
in2_fr1.grid(row= 2, column= 1,columnspan= 2, sticky=NE)

#CPF
lb4_fr1.grid(row= 3, column= 0,sticky=NE)
in3_fr1.grid(row= 3, column= 1,columnspan= 2, sticky=NE)

#Telefone
lb5_fr1.grid(row= 4, column= 0,sticky=NE)
in4_fr1.grid(row= 4, column= 1,columnspan= 2, sticky=NE)

#Endereço/rua
lb6_fr2.grid(row= 0, column= 0,)
lb7_fr2.grid(row= 1, column= 0, sticky=NE)
in5_fr2.grid(row= 1, column= 1, columnspan=4, sticky=NSEW)

#bairro
lb8_fr2.grid(row= 2, column= 0, sticky=NE)
in6_fr2.grid(row= 2, column= 1, sticky=NSEW)

#cidade
lb9_fr2.grid(row= 2, column= 2, sticky=NSEW)
in7_fr2.grid(row= 2, column= 3, sticky=NSEW)

#n°
lb10_fr2.grid(row= 1, column= 4, sticky=NSEW)
in8_fr2.grid(row= 1, column= 5, sticky=NSEW)

#UF
lb11_fr2.grid(row=2, column= 4, sticky=NSEW)
in9_fr2.grid(row= 2, column= 5, sticky=NSEW)

#Botão
bt1_fr3.grid(row=0, column=0)
bt2_fr3.grid(row=0, column=1)

#executar e manter janela aberta
root.mainloop()