from tkinter import *

#back-end
def imprimir():
    z = int(num1.get()) + int(num2.get())
    lb3['text'] = z



#front-end


#window
janela = Tk()

#geometria
janela.geometry('400x300+720+360')
janela.config(bg= 'black',)
janela.minsize(width=100, height=100)
janela.maxsize(width=600, height=600)



#widget
lb1 = Label(janela, text='Calculadora',
            font='Arial 26',
            foreground='purple')
num1 = Entry(janela, font='Arial 26')
lb2 = Label(janela, text='+')
num2 = Entry(janela, font='Arial 26')
lb3 = Label(janela, text='',
            font='Arial 20',
            foreground='blue')
bt1 = Button(janela, text='Soma', font='Arial 26', command=imprimir)

#layout
lb1.pack()
num1.pack()
lb2.pack()
num2.pack()
bt1.pack()
lb3.pack()

#rum
janela.mainloop()