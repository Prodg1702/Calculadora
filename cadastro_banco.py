from tkinter import *

#criando janela
root = Tk()
root.title('Login / Cadastro')
root.geometry('1480x500+300+150')
root.config(bg='#10929c')
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)


fr3 = LabelFrame(root, text='Login / Cadastro', background='#10929c')
fr3_1 = LabelFrame(root, text='Cadastro', background='#10929c')

#criando widgets
lb0_fr3 = Label(fr3, text='Bem Vindo ao Dellux', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb1_fr3 = Label(fr3, text='O que deseja fazer?', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb2_fr3 = Label(fr3, text='Usuário:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb3_fr3 = Label(fr3, text='Senha:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in0_fr3 = Entry(fr3,text='', font='Arial 20', background='#10929c')
in1_fr3 = Entry(fr3,text='', font='Arial 20', background='#10929c')



#widgets j2
lb4_fr3_1 = Label(fr3_1, text='Bem vindo a área de cadastro', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb5_fr3_1 = Label(fr3_1, text='Nome:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb6_fr3_1 = Label(fr3_1, text='Data de Nasc:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb7_fr3_1 = Label(fr3_1, text='CPF:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb8_fr3_1 = Label(fr3_1, text='Telefone:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb9_fr3_1 = Label(fr3_1, text='Endereço:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb10_fr3_1 = Label(fr3_1, text='Cidade:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb11_fr3_1 = Label(fr3_1, text='UF:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb12_fr3_1 = Label(fr3_1, text='N°:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb13_fr3_1 = Label(fr3_1, text='Email:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in2_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in3_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in4_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in5_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in6_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in7_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in8_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in9_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in10_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')





#botões
bt0_fr3 = Button(fr3, text='Login', font='Arial 20', background='#10929c', foreground='#f5f5f5')
bt1_fr3 = Button(fr3, text='Cadastro', font='Arial 20', background='#10929c', foreground='#f5f5f5')
bt2_fr3_1 = Button(fr3_1, text='Salvar')
bt3_fr3_1 = Button(fr3_1, text='Voltar')



#frames
fr3.grid(padx=5)
fr3_1.grid(padx=5)



#organizando widgets
lb0_fr3.grid(row=0, column=0, sticky=NSEW)
lb1_fr3.grid(row=1, column=0, sticky=NSEW)
lb2_fr3.grid(row=2, column=0, sticky=NE)
lb3_fr3.grid(row=3, column=0, sticky=NE)
in0_fr3.grid(row=2, column=1, sticky=NSEW)
in1_fr3.grid(row=3, column=1, sticky=NSEW)
bt0_fr3.grid(row=4, column=0, sticky=NSEW)
bt1_fr3.grid(row=4, column=1, sticky=NSEW)

#organizando widgets j2
lb4_fr3_1.grid(row=0, column=0)


#Nome
lb5_fr3_1.grid(row=1, column=0, sticky=NE)
in2_fr3_1.grid(row=1, column=1, columnspan=4, sticky=NSEW)

#Data nasc
lb6_fr3_1.grid(row=2, column=0, sticky=NE)
in3_fr3_1.grid(row=2, column=1) 

#CPF
lb7_fr3_1.grid(row=2, column=2, sticky=NE)
in4_fr3_1.grid(row=2, column=3)  


#Telefone
lb8_fr3_1.grid(row=2, column=4, sticky=NE)
in5_fr3_1.grid(row=2, column=5) 


#Endereço
lb9_fr3_1.grid(row=3, column=0, sticky=NE)
in6_fr3_1.grid(row=3, column=1)


#Cidade
lb10_fr3_1.grid(row=4, column=0, sticky=NE)
in7_fr3_1.grid(row=4, column=1) 


#UF
lb11_fr3_1.grid(row=4, column=2, sticky=NE)
in8_fr3_1.grid(row=4, column=3) 


#N°
lb12_fr3_1.grid(row=4, column=4, sticky=NE)
in9_fr3_1.grid(row=4, column=5)


#Email
lb13_fr3_1.grid(row=5, column=0, sticky=NE)
in10_fr3_1.grid(row=5, column=1, columnspan=4, sticky=NSEW)








root.mainloop()