from tkinter import *
from tkcalendar import Calendar 
import datetime 
root = Tk() 
root.geometry("400x400") 
cal = Calendar(root, selectmode='day', 
               year=2022, month=6, 
               day=8) 
  
cal.pack(pady=20) 
  
frame1 = Frame() 
frame2 = Frame() 
  
frame1.pack() 
frame2.pack() 
Label(frame1, text="Days", bd=1, bg="white", width=20, 
      relief="solid", font="italic 10 bold").pack(side=LEFT) 
days = Spinbox(frame1, from_=0, to=10000000, font="italic 10") 
days.pack(pady=20, padx=10) 
Button(frame2, text="Add Days", font="italic 15").pack(side=LEFT) 
Button(frame2, text="Subtract Days", font="italic 15").pack(padx=10) 
converted_date = Label(text="Date: ", bd=2, bg="white", relief="solid", 
                       font="italic 10 bold", width=30) 
converted_date.pack(pady=20) 
root.mainloop() 