from tkinter import *
from tkinter import Tk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)

bgimage=ImageTk.PhotoImage(file="cargoimg.jpeg")
bglabel=Label(root,image=bgimage)
bglabel.place(x=0,y=0)

label2=Label(text="Cargo Management System",font=("Zen Dots",20,"bold"),fg="gray",bg="white")
label2.place(x=110,y=200)


label1=Label(text="Are you an employee and admin",font=("Herlad",17,"bold"),bg="white")
label1.place(x=115,y=290)

ButtonEmp=Button(text="Employee",font=("Herlad",17,"bold"),height=2,bd=0,bg="grey")
ButtonEmp.place(x=120,y=380)

Buttonadm=Button(text="   Admin    ",font=("Herlad",17,"bold"),height=2,bd=0,bg="grey")
Buttonadm.place(x=320,y=380)



root.mainloop()