# importar biblioteca
from tkinter import *

def calc():
    if in1.get().replace(".","",1).isdigit() and in3.get().replace(".", "", 1).isdigit():
        x = float(in1.get()) / (float(in3.get())*2)
        lb9['text'] = x

    if x <18.5:
        lb12['text'] = "Abaixo do peso"
    elif x >18.5 and x < 24.9:
        lb12['text'] = "Peso ideal"
    elif x > 25 and x < 29.9:
        lb12['text'] = "Sobrepeso"
    elif x > 30 and x < 34.9:
        lb12['text'] = "Obesidade grau I"
    elif x > 35 and x < 39.9:
        lb12['text'] = "Obesidade grau II"
    else:
        lb12['text'] = "Obesidade grau III"





# criar janela
root = Tk()
root.geometry('400x10+720+350') # Declarando o tamanho da janela (400x300) tamanho inicial/ +100 +100 luigar onde ela vai abrir
root.config(bg='grey') # Background color
root.minsize(width=180, height=150)
root.maxsize(width=600, height=600)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


# Criar os widgets

lb1 = Label(root, text='IMC', font='Arial 20')
lb2 = Label(root, text='Peso:')
in1 = Entry(root, text='')
in3 = Entry(root, text='')
lb4 = Label(root, text='Altura:')
lb5 = Label(root, text='')
lb6 = Label(root, text='')
bt1 = Button(root, text='Calcular', command=calc)
lb7 = Label(root, text='')
lb8 = Label(root, text='')
lb9 = Label(root, text='seu imc aqui')
lb10 = Label(root, text='')
lb11 = Label(root, text='')
lb12 = Label(root, text='você está')
lb13 = Label(root, text='')
lb14 = Label(root, text='')


# Organizar os widgets
lb1.grid(row=0, column=0, columnspan=3, sticky=NSEW)
lb2.grid(row=1, column=0, sticky=NSEW)
in1.grid(row=1, column=1, sticky=NSEW)
in3.grid(row=2, column=1, sticky=NSEW)
lb4.grid(row=2, column=0, sticky=NSEW)
lb5.grid(row=2, column=2, sticky=NSEW)
lb6.grid(row=1, column=2, sticky=NSEW)
lb7.grid(row=3, column=0, sticky=NSEW)
lb8.grid(row=3, column=2, sticky=NSEW)
bt1.grid(row=3, column=1, sticky=NSEW)
lb9.grid(row=4, column=1, sticky=NSEW)
lb10.grid(row=4, column=0, sticky=NSEW)
lb11.grid(row=4, column=2, sticky=NSEW)
lb12.grid(row=5, column=1, sticky=NSEW)
lb13.grid(row=5, column=0, sticky=NSEW)
lb14.grid(row=5, column=2, sticky=NSEW)

# Executar e manter a janela
root.mainloop()