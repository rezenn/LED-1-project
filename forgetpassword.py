from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as mysql
import tkinter.messagebox as messagebox

def update_login_info():
    #update passwords and information of the user
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    new_password = new_password_entry.get()
    confirm_password = password2_entry.get()

    if name == "" or email == "" or contact == "" or new_password == "" or confirm_password == "":
        messagebox.showerror("Error", "Insert all values")
    elif new_password != confirm_password:
        messagebox.showinfo("Error", "The password does not match !!!")
    else:

        con = mysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="cargo_mngt"
        )
        cursor = con.cursor()

        # Use parameterized query to prevent SQL injection
        cursor.execute("UPDATE register SET password=%s, confirm_password=%s WHERE email=%s",
                       (new_password, confirm_password, email))

        con.commit()
        messagebox.showinfo("Status", "Successfully updated")
        con.close()
        clear()

def clear():
    # Define the clear function to clear entry fields
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    contact_entry.delete(0, END)
    new_password_entry.delete(0, END)
    password2_entry.delete(0, END)

def password_visual():
    # Show and hide password with eye button
    if new_password_entry.cget("show") == '':
        new_password_entry.config(show='*')
        showhide.config(image=showimg)
    else:
        new_password_entry.config(show="")
        showhide.config(image=hideimg) 

def password_visual2():
    if password2_entry.cget("show") == '':
        password2_entry.config(show='*')
        showhide2.config(image=showimg2)
    else:
        password2_entry.config(show="")
        showhide2.config(image=hideimg2) 

def log_in():
    root.destroy()
    import Employeelogin

#GUI part
    
root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Reset password')
root.iconbitmap("cargo_icon.ico")

bgimage = ImageTk.PhotoImage(file="log102.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

company_name = Label(root, text="Cargo Management System", font=("Herald", 22), bg="#e0dcdc")
company_name.place(x=100, y=190)

register_label = Label(root, text="Reset Password", font=("Herald", 21, "bold"), bg="#e0dcdc")
register_label.place(x=180, y=230)

name_label = Label(root, text="Name :",font=("Herald", 11),bg="#e0dcdc")
name_label.place(x=100, y=300)
name_entry = Entry(root, width=35,bg="#d9d9d9")
name_entry.place(x=255, y=300)


contact_label = Label(root, text="Contact :",font=("Herald", 11),bg="#e0dcdc")
contact_label.place(x=100, y=335)
contact_entry = Entry(root, width=35,bg="#d9d9d9")
contact_entry.place(x=255, y=335)

email_label = Label(root, text="Email :",font=("Herald", 11),bg="#e0dcdc")
email_label.place(x=100, y=370)
email_entry = Entry(root, width=35,bg="#d9d9d9")
email_entry.place(x=255, y=370)

new_password_label = Label(root, text="New password :",font=("Herald", 11), bg="#e0dcdc")
new_password_label.place(x=100, y=405)
new_password_entry = Entry(root, width=35,bg="#d9d9d9", show='*')
new_password_entry.place(x=255, y=405)

# eye image
showimg = PhotoImage(file='show_eye.png')
hideimg = PhotoImage(file="hide_eye.png")
showhide = Button(root, image=showimg, width=22, height=14, command=password_visual, fg='white',bg="#e0dcdc", bd=0)
showhide.place(x=445, y=407)

password2_label = Label(root, text="confirm Password :",font=("Herald", 11),bg="#e0dcdc")
password2_label.place(x=100, y=440)
password2_entry = Entry(root, width=35,bg="#d9d9d9", show='*')
password2_entry.place (x=255, y=440)

# eye image
showimg2 = PhotoImage(file='show_eye.png')
hideimg2 = PhotoImage(file="hide_eye.png")
showhide2 = Button(root, image=showimg, width=22, height=14, command=password_visual2, fg='white', bg='#e0dcdc', bd=0)
showhide2.place(x=445, y=442)

Updatepassword = Button(root,width=33, text="Update Password",font=("Herald", 13),bg="#000000",fg="#ffffff",command=update_login_info)
Updatepassword.place(x=135, y=500)

login=Button(root,width=33,text="Login",bg="#000000",font=("Herald", 13),fg="#ffffff",command=log_in)
login.place(x=135,y=550)



root.mainloop()

