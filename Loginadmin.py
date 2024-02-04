from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def password_visual():
    if passwordEntry.cget("show") == '':
        passwordEntry.config(show='*')
        showhide.config(image=showimg)
    else:
        passwordEntry.config(show="")
        showhide.config(image=hideimg)

def home():
    root.destroy()
    import Employeelogin        

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Login Page')

bgimage = ImageTk.PhotoImage(file="log102.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)


Frame1=Frame(root, height="480",width="420", bg="#e0dcdc")
Frame1.place(x=80, y=215)

# headingsfor 3 
heading1 = Label(root, text='Cargo Management System', font=("Zen Dots", 20), bg="#e0dcdc")
heading1.place(x=112, y=200)

heading2 = Label(root, text='Log In as Admin', font=("Rubik one", 24, "bold"), bg="#e0dcdc")
heading2.place(x=158, y=250)

heading3 = Label(root, text='Enter your username and password below', font=("Arial", 9), bg="#e0dcdc")
heading3.place(x=163, y=310)

# username
username = Label(root, text='USERNAME', font=("Zen Dots", 7, "bold"), bg="#e0dcdc")
username.place(x=135, y=365)

usernameEntry = Entry(root, width=32, font=('Herald', 13))
usernameEntry.place(x=135, y=380)

# password
passwordLabel = Label(root, text='PASSWORD', font=("Zen Dots", 7, "bold"), bg="#e0dcdc")
passwordLabel.place(x=135, y=425)

passwordEntry = Entry(root, width=32, font=('Herald', 13), show='*')
passwordEntry.place(x=135, y=440)

# eye image
showimg = PhotoImage(file='show_eye.png')
hideimg = PhotoImage(file="hide_eye.png")
showhide = Button(root, image=showimg, width=25, height=22, command=password_visual, fg='white', bg='#FFFFFF', bd=0)
showhide.place(x=403, y=440)

# forgot password
forgotbutton = Button(root, text='Forgot Password?', font=("Arial", 7, "bold"), bg="#e0dcdc", fg="firebrick1",
                      cursor="hand2", activeforeground="firebrick1", bd=0)
forgotbutton.place(x=335, y=470)

# login button
loginbutton = Button(root, text="Log in", font=("Open Sans", 13, "bold"), bg="black", fg="White", cursor="hand2",
                    activeforeground="black", bd=0, width=28,command=home)
loginbutton.place(x=135, y=520)



root.mainloop()
