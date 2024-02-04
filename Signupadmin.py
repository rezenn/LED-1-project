from tkinter import*
from PIL import Image,ImageTk

signupadmin_window=Tk()
signupadmin_window.title('Signup Page Admin')
background=ImageTk.PhotoImage(file='log102.jpg')


bgLabel=Label(signupadmin_window,image=background)
bgLabel.grid()


heading1= Label(signupadmin_window, text='Cargo Management System', font=("Zen Dots", 20),bg="#e0dcdc")
heading1.place(x=112, y=200)

heading2= Label(signupadmin_window, text='Register', font=("Rubik one", 24, "bold"),bg="#e0dcdc")
heading2.place(x=158, y=250)

signupadmin_window.mainloop()