# importar biblioteca
from tkinter import *

def aumentar():
    if lb1['text'] <10:
        lb1['text'] += 1
    else:
        pass

def diminuir():
    if lb1['text'] > -10:
        lb1['text'] -= 1
    else:
        pass



# criar janela
root = Tk()
root.geometry('400x10+720+350') # Declarando o tamanho da janela (400x300) tamanho inicial/ +100 +100 luigar onde ela vai abrir
root.config(bg='black') # Background color desejada
root.minsize(width=100, height=56)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


# Criar os widgets
bt1 = Button(root, text='-', width=10, height=3, command=diminuir)
lb1 = Label(root, text= 0, width=10)
bt2 = Button(root, text='+', width=10, height=3, command=aumentar)


# Organizar os widgets
bt1.grid(row=0, column=0, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)

# Executar e manter a janela
root.mainloop()