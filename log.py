from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql
  

def login():
    win.destroy()
    import login

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
            win.destroy()
            import contact

win=Tk()
win.geometry("500x500")
win.title("Log in")

cargo=Label(win,text="Cargo Management System",font=("The Times New Roman",20))
cargo.grid(row=5, column=4,columnspan=3)
email=Label(win,text="email")
email.grid(row=7,column=4)
email_entry=Entry(win)
email_entry.grid(row=7,column=5)
password=Label(win,text="Password")
password.grid(row=9,column=4)
password_entry=Entry(win)
password_entry.grid(row=9,column=5)
register=Button(win,text="Register",command=login)
register.grid(row=11,column=5)

login=Button(win,text="Login",command=login_user)
login.grid(row=13,column=5)
win.mainloop()