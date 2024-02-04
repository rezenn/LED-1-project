from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

      

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Login Page')

bgimage = ImageTk.PhotoImage(file="log102.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

company_name= Label(root, text="Cargo Management System",font=("Herald", 22),bg="#e0dcdc")
company_name.place(x=100,y=190)

register_label= Label(root, text="Reset Password",font=("Herald", 21, "bold"),bg="#e0dcdc")
register_label.place(x=180,y=230)

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
new_password_entry = Entry(root, width=35,bg="#d9d9d9")
new_password_entry.place(x=255, y=405)

password2_label = Label(root, text="Conform Password :",font=("Herald", 11),bg="#e0dcdc")
password2_label.place(x=100, y=440)
password2_entry = Entry(root, width=35,bg="#d9d9d9")
password2_entry.place (x=255, y=440)

Updatepassword = Button(root,width=33, text="Update Password",font=("Herald", 13),bg="#000000",fg="#ffffff")
Updatepassword.place(x=135, y=500)

login=Button(root,width=33,text="Login",bg="#000000",font=("Herald", 13),fg="#ffffff")
login.place(x=135,y=550)



root.mainloop()
