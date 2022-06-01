# importando a biblioteca
from tkinter import *

#calculo
def calculo():
    if in1.get().replace(".","",1).isdigit():
        x = float(in1.get()) * 1.8 + 32
        lb3['text'] = x
    else:
        lb3['text'] = "Tente novamente"

    
    

#criando janela
root = Tk()
root.geometry('400x10+720+350') # Declarando o tamanho da janela (400x300) tamanho inicial/ +100 +100 luigar onde ela vai abrir
root.config(bg='grey') # Background color
root.minsize(width=180, height=160)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


#criando widgets
lb1 = Label(root, text='Conversor de temperatura', font='Arial 20')
lb2 = Label(root, text='°C', font='Arial 20')
in1 = Entry(root, text='')
bt1 = Button(root, text='°F', font='Arial 20', command=calculo)
lb3 = Label(root, text='')
lb4 = Label(root, text='')
lb5 = Label(root, text='')


#organização widgets
lb1.grid(row=0, column=0, columnspan=3, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
in1.grid(row=1, column=1, sticky=NSEW)
lb4.grid(row=1, column=2, sticky=NSEW)
bt1.grid(row=2, column=0, sticky=NSEW)
lb3.grid(row=2, column=1, sticky=NSEW)
lb5.grid(row=2, column=2, sticky=NSEW)


#executar e manter janela
root.mainloop()