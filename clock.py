from tkinter import *
from datetime import datetime
import tkinter

#define some colors
cor1="#000000"  # background color _ black
cor2="#b0bf1a"  # yellow

root=Tk()
root.title("")
root.geometry('450x180')
root.resizable(width=FALSE,height=FALSE)
root.configure(background=cor1)


def clock():
    time = datetime.now()
    hour =time.strftime("%H:%M:%S")
    weekday=time.strftime("%A")
    day=time.day
    month=time.strftime("%b")
    year=time.strftime("%Y")

    l1.config(text=hour)
    l1.after(200,clock)


    l2.config(text=weekday + "\t" + str(day) + "/" +str(month) + "/" + (year))



l1=Label(root, font=('Arial 60'), bg=cor1,fg=cor2)
l1.grid(row=0,column=0,sticky=NW)


l2=Label(root,font=('Arial 20'), bg=cor1,fg=cor2)
l2.grid(row=1,column=0,sticky=NW)


clock()
root.mainloop()
