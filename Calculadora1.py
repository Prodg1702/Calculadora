from tkinter import *

#criando ação
def entrada(valor):
    lb1['text'] += valor

def limpar():
    lb1['text'] = ''

def resultado():
    x = eval(lb1['text'])
    lb1['text'] = x

#criando janela
root = Tk()
root.title('Calculadora')
root.geometry('400x10+720+350')
root.config(bg='grey')
root.minsize(width=400, height=360)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)


#vincular teclado
root.bind('1', lambda event: entrada('1'))
root.bind('2', lambda event: entrada('2'))
root.bind('3', lambda event: entrada('3'))
root.bind('4', lambda event: entrada('4'))
root.bind('5', lambda event: entrada('5'))
root.bind('6', lambda event: entrada('6'))
root.bind('7', lambda event: entrada('7'))
root.bind('8', lambda event: entrada('8'))
root.bind('9', lambda event: entrada('9'))
root.bind('0', lambda event: entrada('0'))
root.bind('+', lambda event: entrada('+'))
root.bind('-', lambda event: entrada('-'))
root.bind('*', lambda event: entrada('*'))
root.bind('/', lambda event: entrada('/'))
root.bind('<Return>', lambda event: resultado())

#criando widgets
lb1 = Label(root, text='', font='Arial 25')
bt1 = Button(root, text='1', font='Arial 20', command=lambda: entrada('1'))
bt2 = Button(root, text='2', font='Arial 20', command=lambda: entrada('2'))
bt3 = Button(root, text='3', font='Arial 20', command=lambda: entrada('3'))
bt4 = Button(root, text='4', font='Arial 20', command=lambda: entrada('4'))
bt5 = Button(root, text='5', font='Arial 20', command=lambda: entrada('5'))
bt6 = Button(root, text='6', font='Arial 20', command=lambda: entrada('6'))
bt7 = Button(root, text='7', font='Arial 20', command=lambda: entrada('7'))
bt8 = Button(root, text='8', font='Arial 20', command=lambda: entrada('8'))
bt9 = Button(root, text='9', font='Arial 20', command=lambda: entrada('9'))
bt10 = Button(root, text='0', font='Arial 20', command=lambda: entrada('0'))

#widgets de simbologia
bt11 = Button(root, text='+', font='Arial 20', command=lambda: entrada('+'))
bt12 = Button(root, text='-', font='Arial 20', command=lambda: entrada('-'))
bt13 = Button(root, text='*', font='Arial 20', command=lambda: entrada('*'))
bt14 = Button(root, text='/', font='Arial 20', command=lambda: entrada('/'))
bt15 = Button(root, text='=', font='Arial 20', command= resultado)
bt16 = Button(root, text='C', font='Arial 20', command= limpar)



#organização dos widgets
lb1.grid(row=0, column=0, columnspan=4, sticky=NSEW)
bt1.grid(row=3, column=0, sticky=NSEW)
bt2.grid(row=3, column=1, sticky=NSEW)
bt3.grid(row=3, column=2, sticky=NSEW)
bt4.grid(row=2, column=0, sticky=NSEW)
bt5.grid(row=2, column=1, sticky=NSEW)
bt6.grid(row=2, column=2, sticky=NSEW)
bt7.grid(row=1, column=0, sticky=NSEW)
bt8.grid(row=1, column=1, sticky=NSEW)
bt9.grid(row=1, column=2, sticky=NSEW)
bt10.grid(row=4, column=1, sticky=NSEW)
bt11.grid(row=3, column=3, sticky=NSEW)
bt12.grid(row=2, column=3, sticky=NSEW)
bt13.grid(row=1, column=3, sticky=NSEW)
bt14.grid(row=4, column=2, sticky=NSEW)
bt15.grid(row=4, column=3, sticky=NSEW)
bt16.grid(row=4, column=0, sticky=NSEW)




#abrindo e mantendo janela
root.mainloop()