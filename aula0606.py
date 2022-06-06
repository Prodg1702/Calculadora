from tkinter import *

#criando janela
root = Tk()
root.geometry('400x10+720+350')
root.minsize(width=400, height=360)
root.maxsize(width=600, height=600)

fr1 = Frame(root, background='black')
fr2 = Frame(root, background='grey')

#criando widgets
lb1_fr1 = Label(fr1, text='Label no frame 1', font='Arial 25')
lb1_fr2 = Label(fr2, text='Label no frame 2', font='Arial 25')
bt1_fr1 = Button(fr1, text='Bt no label 1', font='Arial 25')
bt1_fr2 = Button(fr2, text='Bt no label 2', font='Arial 25')

fr1.pack()
fr2.pack()

#organizando widget
lb1_fr1.grid(row=0, column=0)
bt1_fr1.grid(row=1, column=1)
lb1_fr2.grid(row=0, column=0)
bt1_fr2.grid(row=1, column=1)

#mantendo janela aberta
root.mainloop()