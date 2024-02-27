from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql


def admin_log():
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

        query = "SELECT * FROM admin WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        row = cursor.fetchone()

        if row is None:
            messagebox.showerror("Error", "Invalid entry")
        else:
            root.destroy()
            import dashboard        

def password_visual():
    # Show and hide password with eye button
    if password_entry.cget("show") == '':
        password_entry.config(show='*')
        showhide.config(image=showimg)
    else:
        password_entry.config(show="")
        showhide.config(image=hideimg)       

#GUI part
        
root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Login Page')
root.iconbitmap('cargo_icon.ico')

bgimage = ImageTk.PhotoImage(file="log102.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)


Frame1=Frame(root, height="480",width="420", bg="#e0dcdc")
Frame1.place(x=80, y=215)

# headings
heading1 = Label(root, text='Cargo Management System', font=("Zen Dots", 20), bg="#e0dcdc")
heading1.place(x=112, y=200)

heading2 = Label(root, text='Log In as Admin', font=("Rubik one", 24, "bold"), bg="#e0dcdc")
heading2.place(x=158, y=250)

heading3 = Label(root, text='Enter your username and password below', font=("Arial", 9), bg="#e0dcdc")
heading3.place(x=163, y=310)

# username
email_label = Label(root, text='Email', font=("Zen Dots", 7, "bold"), bg="#e0dcdc")
email_label.place(x=135, y=365)

email_entry = Entry(root, width=32, font=('Herald', 13))
email_entry.place(x=135, y=380)

# password
password_label = Label(root, text='Password', font=("Zen Dots", 7, "bold"), bg="#e0dcdc")
password_label.place(x=135, y=425)

password_entry = Entry(root, width=32, font=('Herald', 13), show='*')
password_entry.place(x=135, y=440)

# eye image
showimg = PhotoImage(file='show_eye.png')
hideimg = PhotoImage(file="hide_eye.png")
showhide = Button(root, image=showimg, width=25, height=19, command=password_visual, fg='white', bg='#FFFFFF', bd=0)
showhide.place(x=400, y=442)


# login button
loginbutton = Button(root, text="Log in", font=("Open Sans", 13, "bold"), bg="black", fg="White", cursor="hand2",
                    activeforeground="black", bd=0, width=28,command=admin_log)
loginbutton.place(x=135, y=520)



root.mainloop()
