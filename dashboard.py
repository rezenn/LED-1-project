from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def employee():
    root.destroy()
    import employee

def about_us():
    root.destroy()
    import about

def contact_us():
    root.destroy()
    import contact

def add_new_cargo():
    root.destroy()
    import addnewcargo




root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Dashboard')
root.iconbitmap("cargo_icon.ico")

#heading

Label1=Label(root,text="Dashboard",font=("Rubik one",20),bg="#Faeded")
Label1.place(x=265,y=30)

#frame

Frame1=Frame(root,height="590",width="900",bg="#e0dcdc")
Frame1.place(x=260,y=80)





framef=Frame(root,height="140",width="190",bg="gray")
framef.place(x=300,y=120)

frame2=Frame(root,height="140",width="190",bg="gray")
frame2.place(x=620,y=120)

frame3=Frame(root,height="140",width="190",bg="gray")
frame3.place(x=940,y=120)

frame4=Frame(root,height="140",width="190",bg="gray")
frame4.place(x=300,y=320)

frame5=Frame(root,height="140",width="190",bg="gray")
frame5.place(x=620,y=320)

frame6=Frame(root,height="140",width="190",bg="gray")
frame6.place(x=940,y=320)









#leftside

Frame2=Frame(root,height="800",width="210",bg="#363740")
Frame2.place(x=0,y=1)

cargo=Label(root, text="Cargo Management System", font=('Rubik one', 10, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=28,y=2)

dashboard=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc")
dashboard.place(x=1,y=80)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white',
                    bd=0, cursor="hand2", activebackground="#e0dcdc",command=add_new_cargo)
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc",)
Viewcargo.place(x=1,y=178)

cargotype=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)

employees=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
employees.place(x=1,y=276)

Aboutus=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=about_us)
Aboutus.place(x=1,y=325)

contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contactus.place(x=1,y=374)

Subscription=Button(root, text="Subscription", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                     bd=0, cursor="hand2", activebackground="#e0dcdc")
Subscription.place(x=1,y=450)


root.mainloop()