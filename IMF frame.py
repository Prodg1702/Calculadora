from tkinter import *

#calculo
def calc():
    if in1_fr1.get().replace(".","",1).isdigit() and in3_fr1.get().replace(".", "", 1).isdigit():
        x = float(in1_fr1.get()) / (float(in3_fr1.get())*2)
        lb9_fr2['text'] = x

    if x <18.5:
        lb12_fr2['text'] = "Abaixo do peso"
    elif x >18.5 and x < 24.9:
        lb12_fr2['text'] = "Peso ideal"
    elif x > 25 and x < 29.9:
        lb12_fr2['text'] = "Sobrepeso"
    elif x > 30 and x < 34.9:
        lb12_fr2['text'] = "Obesidade grau I"
    elif x > 35 and x < 39.9:
        lb12_fr2['text'] = "Obesidade grau II"
    else:
        lb12_fr2['text'] = "Obesidade grau III"





# criar janela
root = Tk()
root.geometry('400x155+720+350') # Declarando o tamanho da janela (400x300) tamanho inicial/ +100 +100 luigar onde ela vai abrir

fr1 = Frame(root, background='#dcdcdc')
fr2 = Frame(root, background='#dcdcdc')


# Criar os widgets

lb1_fr1 = Label(fr1, text='IMC', font='Arial 20')
lb2_fr1 = Label(fr1, text='Peso:')
in1_fr1 = Entry(fr1, text='')
in3_fr1 = Entry(fr1, text='')
lb4_fr1 = Label(fr1, text='Altura:')
lb5_fr1 = Label(fr1, text='')
lb6_fr1 = Label(fr1, text='')
bt1_fr2 = Button(fr2, text='Calcular', command=calc)
lb7_fr2 = Label(fr2, text='')
lb8_fr2 = Label(fr2, text='')
lb9_fr2 = Label(fr2, text='seu imc aqui')
lb10_fr2 = Label(fr2, text='')
lb11_fr2 = Label(fr2, text='')
lb12_fr2 = Label(fr2, text='você está')
lb13_fr2 = Label(fr2, text='')
lb14_fr2 = Label(fr2, text='')


fr1.pack()
fr2.pack()

# Organizar os widgets
lb1_fr1.grid(row=0, column=0, columnspan=3, stick=NSEW)
lb2_fr1.grid(row=1, column=0, sticky=NSEW)
in1_fr1.grid(row=1, column=1, sticky=NSEW)
in3_fr1.grid(row=2, column=1, sticky=NSEW)
lb4_fr1.grid(row=2, column=0, sticky=NSEW)
lb5_fr1.grid(row=2, column=2, sticky=NSEW)
lb6_fr1.grid(row=1, column=2, sticky=NSEW)
lb7_fr2.grid(row=0, column=0, sticky=NSEW)
lb8_fr2.grid(row=0, column=2, sticky=NSEW)
bt1_fr2.grid(row=0, column=1, sticky=NSEW)
lb9_fr2.grid(row=1, column=1, sticky=NSEW)
lb10_fr2.grid(row=1, column=0, sticky=NSEW)
lb11_fr2.grid(row=1, column=2, sticky=NSEW)
lb12_fr2.grid(row=2, column=1, sticky=NSEW)
lb13_fr2.grid(row=2, column=0, sticky=NSEW)
lb14_fr2.grid(row=2, column=2, sticky=NSEW)

# Executar e manter a janela
root.mainloop()