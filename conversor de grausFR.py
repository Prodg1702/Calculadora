# importando a biblioteca
from tkinter import *

#calculo
def calculo():
    if in1_fr1.get().replace(".","",1).isdigit():
        x = float(in1_fr1.get()) * 1.8 + 32
        lb3_fr2['text'] = x
    else:
        lb3_fr2['text'] = "Tente novamente"

    
    

#criando janela
root = Tk()
root.geometry('400x200+720+350')
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)


fr1 = Frame(root, background='#dcdcdc')
fr2 = Frame(root, background='#dcdcdc')

#criando widgets
lb1_fr1 = Label(fr1, text='Conversor de temperatura', font='Arial 20')
lb2_fr1 = Label(fr1, text='°C', font='Arial 20')
in1_fr1 = Entry(fr1, text='')
bt1_fr2 = Button(fr2, text='°F', font='Arial 20', command=calculo)
lb3_fr2 = Label(fr2, text='')
lb4_fr2 = Label(fr2, text='')
lb5_fr2 = Label(fr2, text='')

fr1.pack()
fr2.pack()


#organização widgets
lb1_fr1.grid(row=0, column=0, columnspan=3, sticky=NSEW)
lb2_fr1.grid(row=1, column=0, sticky=NSEW)
in1_fr1.grid(row=1, column=1, sticky=NSEW)
lb4_fr2.grid(row=1, column=2, sticky=NSEW)
bt1_fr2.grid(row=0, column=0, sticky=NSEW)
lb3_fr2.grid(row=0, column=1, sticky=NSEW)
lb5_fr2.grid(row=0, column=2, sticky=NSEW)


#executar e manter janela
root.mainloop()