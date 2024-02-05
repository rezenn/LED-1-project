from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from PIL import ImageTk
from validate_email_address import validate_email


# Function to check if the email is valid
def is_valid_email(email):
    return validate_email(email)

#functions part
def log():
    root.destroy()
    import Employeelogin

def clear():
    name_entry.delete(0,END)
    email_entry.delete(0,END)
    contact_entry.delete(0,END)
    password_entry.delete(0,END)
    password2_entry.delete(0,END)

def create():
    #get data typed by the user
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    password = password_entry.get()
    conform_password = password2_entry.get()
    #show error if the instructions are not followed
    if name == "" or email == "" or contact == "" or password == "" or conform_password == "":
        messagebox.showinfo("ALERT", "Enter every component !!!")

    elif password != conform_password:
        messagebox.showinfo("Error", "The password doesnot match !!!")
    elif not is_valid_email(email):
        messagebox.showinfo("Error", "Invalid email address")
    #excess mysqlworkbench database
    else:
        con = mysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="cargo_mngt"
        )
        cursor = con.cursor()
        #Insert the data into database
        
        cursor.execute("INSERT INTO register (name,contact,email,password,conform_password) VALUES (%s, %s, %s, %s, %s)", (name, contact, email, password, conform_password))
        con.commit()
        messagebox.showinfo("Status", "Successfully registered")
        con.close()
        clear()

#GUI part
root = Tk()
root.title("Registration Form")
root.geometry('1242x776')
root.iconbitmap("cargo_icon.ico")
root.resizable(0,0)

background_img=ImageTk.PhotoImage(file='bg_img.jpg')
bglabel=Label(root,image=background_img)
bglabel.place(x=0,y=0)

logo=ImageTk.PhotoImage(file='logo (1).jpg')
bglabel=Label(root,image=logo)
bglabel.place(x=243,y=140)

company_name= Label(root, text="Cargo Management System",font=("Herald", 22))
company_name.place(x=100,y=200)

register_label= Label(root, text="Register",font=("Herald", 21))
register_label.place(x=220,y=240)

name_label = Label(root, text="Name :",font=("Herald", 11))
name_label.place(x=100, y=300)
name_entry = Entry(root, width=35,bg="#d9d9d9")
name_entry.place(x=255, y=300)


contact_label = Label(root, text="Contact :",font=("Herald", 11))
contact_label.place(x=100, y=335)
contact_entry = Entry(root, width=35,bg="#d9d9d9")
contact_entry.place(x=255, y=335)

email_label = Label(root, text="Email :",font=("Herald", 11))
email_label.place(x=100, y=370)
email_entry = Entry(root, width=35,bg="#d9d9d9")
email_entry.place(x=255, y=370)

password_label = Label(root, text="Password :",font=("Herald", 11))
password_label.place(x=100, y=405)
password_entry = Entry(root, width=35,bg="#d9d9d9")
password_entry.place(x=255, y=405)

password2_label = Label(root, text="Conform Password :",font=("Herald", 11))
password2_label.place(x=100, y=440)
password2_entry = Entry(root, width=35,bg="#d9d9d9")
password2_entry.place (x=255, y=440)

register = Button(root,width=33, text="Register",font=("Herald", 13),bg="#000000",fg="#ffffff", command=create)
register.place(x=120, y=500)

login=Button(root,width=33,text="Login",bg="#000000",font=("Herald", 13),fg="#ffffff",command=log)
login.place(x=120,y=550)


root.mainloop()