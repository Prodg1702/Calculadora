from tkinter import * 

#add ação
def entrada(valor):
    lb1['text'] += valor

def limpar():
    lb1['text'] = ''

#criando janela
root = Tk()

lb1 = Label(root, text='Entrada', font='Arial 25')
bt1 = Button(root, text='A', font='Arial 20', command=lambda: entrada('A'))
bt2 = Button(root, text='B', font='Arial 20', command=lambda: entrada('B'))
bt3 = Button(root, text='C', font='Arial 20', command=lambda: entrada('C'))
bt4 = Button(root, text='LIMP', font='Arial 20', command=limpar)


#criando widgets
lb1.grid(row=0, column=1, columnspan=3, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=2, column=0, sticky=NSEW)
bt3.grid(row=3, column=0, sticky=NSEW)
bt4.grid(row=4, column=0, sticky=NSEW)


#criando e mantendo janela
root.mainloop()