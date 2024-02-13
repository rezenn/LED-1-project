from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')



#heading

Label1=Label(root, text="Employees", font=("Rubik one", 20), bg="#faeded")
Label1.place(x=265, y=30)



#frame

Frame1=Frame(root, height="590",width="900", bg="#e0dcdc")
Frame1.place(x=260, y=80)

employeename=Label(root, text="Employee Name:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
employeename.place(x=300, y=140)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=460, y=140)

employeepost=Label(root, text="Employee post:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
employeepost.place(x=300, y=170)

postentry=Entry(root, width=30, font=("Herald", 11))
postentry.place(x=460, y=170)

Addresssender=Label(root, text="Address:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
Addresssender.place(x=300, y=200)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=460, y=200)


email=Label(root, text="Email:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
email.place(x=300, y=230)

emailentry=Entry(root, width=30, font=("Herald", 11))
emailentry.place(x=460, y=230)


contactsender=Label(root, text="Contact:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
contactsender.place(x=300, y=260)

contactentry=Entry(root, width=30, font=("Herald", 11 ))
contactentry.place(x=460, y=260)

usern=Label(root, text="Username:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
usern.place(x=300, y=290)

usernameentry=Entry(root,width=30, font=("Herald", 11))
usernameentry.place(x=460, y=290)   

id=Label(root, text="Employee ID:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
id.place(x=300, y=320)

eidentry=Entry(root,width=30, font=("Herald", 11))
eidentry.place(x=460, y=320) 

#Button

add=Button(root, text="Add", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1)
add.place(x=350, y=600)

update=Button(root, text="Update", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1)
update.place(x=650, y=600)

delete=Button(root, text="Delete", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1)
delete.place(x=960, y=600)





#left side

Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

cargom=Label(root, text="Cargo Management System", font=('Herald', 11, 'bold'), bg=('#363740'), fg='white')
cargom.place(x=28,y=2)

dashboard=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
dashboard.place(x=1,y=80)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Viewcargo.place(x=1,y=178)

cargotype=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)

employee=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
employee.place(x=1,y=276)

Aboutus=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Aboutus.place(x=1,y=325)

contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
contactus.place(x=1,y=374)

root.mainloop()