from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
  
def forgot_password():
    root.destroy()
    import forgetpassword
def signup():
    root.destroy()
    import register

def login_user():
    # Get values from Entry widgets
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showerror("Error", "Enter both email and password")
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="root"
        )
        cursor = con.cursor()

        # Select the database
        query = "USE cargo_mngt"
        cursor.execute(query)

        query = "SELECT * FROM register WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        row = cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Invalid entry")
        else:
            root.destroy()
            import contact

def password_visual():
    if password_entry.cget("show") == '':
        password_entry.config(show='*')
        showhide.config(image=showimg)
    else:
        password_entry.config(show="")
        showhide.config(image=hideimg)

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Login Page')
root.iconbitmap('cargo_icon.ico')

bgimage = ImageTk.PhotoImage(file="log102.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

# headings
heading1 = Label(root, text='Cargo Management System', font=("Zen Dots", 20), bg="#e0dcdc")
heading1.place(x=112, y=200)

heading2 = Label(root, text='Log In as Employee', font=("Rubik one", 24, "bold"), bg="#e0dcdc")
heading2.place(x=140, y=250)

heading3 = Label(root, text='Enter your username and password below', font=("Arial", 10), bg="#e0dcdc")
heading3.place(x=163, y=310)

# username
email_label = Label(root, text='Email', font=("Herald", 9 ), bg="#e0dcdc")
email_label.place(x=135, y=364)

email_entry = Entry(root, width=32, font=("Herald", 12))
email_entry.place(x=135, y=380)

# password
passwordLabel = Label(root, text='Password', font=("Herald", 9 ), bg="#e0dcdc")
passwordLabel.place(x=135, y=424)

password_entry = Entry(root, width=32, font=("Herald", 12), show='*')
password_entry.place(x=135, y=440)

# eye image
showimg = PhotoImage(file='show_eye.png')
hideimg = PhotoImage(file="hide_eye.png")
showhide = Button(root, image=showimg, width=25, height=17, command=password_visual, fg='white', bg='#FFFFFF', bd=0)
showhide.place(x=400, y=442)

# forgot password
forgotbutton = Button(root, text='Forgot Password?', font=("Arial", 7, "bold"), bg="#e0dcdc", fg="firebrick1",
                      cursor="hand2", activeforeground="firebrick1", bd=0,command=forgot_password)
forgotbutton.place(x=335, y=470)

# login button
loginbutton = Button(root, text="Log in", font=("Open Sans", 13, "bold"), bg="black", fg="White", cursor="hand2",
                     activeforeground="black", bd=0, width=28, command=login_user)
loginbutton.place(x=135, y=520)

# signup button
signupbutton = Button(root, text="Sign Up", font=("Open Sans", 13, "bold"), bg="black", fg="White", cursor="hand2",
                      activeforeground="black", bd=0, width=28,command=signup)
signupbutton.place(x=135, y=565)

root.mainloop()
