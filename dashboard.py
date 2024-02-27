from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox


def invoicedetails():
    root.destroy()
    import invoiceDetails

def employee():
    root.destroy()
<<<<<<< HEAD
    import employees
=======
    import employees 
>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f

def about_us():
    root.destroy()
    import about

def viewcargo():
    root.destroy()
<<<<<<< HEAD
    import View_cargodetails
#test function
=======
    import contact

>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f
def add_new_cargo():
    root.destroy()
    import addnewcargo


   



def log_out():
    msg_box = messagebox.askquestion('Log out Application', 'Are you sure you want to exit the application?',
                                        icon='warning')
    if msg_box == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the application screen')

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Dashboard')
root.iconbitmap("cargo_icon.ico")

<<<<<<< HEAD
#bgimage = ImageTk.PhotoImage(file="dashboard.jpg")
#bgLabel = Label(root, image=bgimage)
#bgLabel.place(x=0, y=0)
=======
bgimage = ImageTk.PhotoImage(file="dashboard.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)

>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f
#heading

Label1=Label(root,text="Dashboard",font=("Rubik one",20),bg="#Faeded")
Label1.place(x=195,y=53)



#frame
Frame1=Frame(root, height="585",width="930", bg="#e0dcdc")
Frame1.place(x=165, y=100)
tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=169,y=100,width=920,height=580)




<<<<<<< HEAD


framef=Frame(root,height="140",width="191",bg="gray")
framef.place(x=215,y=132)
=======

framef=Frame(root,height="140",width="190",bg="gray")
framef.place(x=300,y=120)

frame2=Frame(root,height="140",width="190",bg="gray")
frame2.place(x=620,y=120)
>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f


frame2=Frame(root,height="140",width="191",bg="gray")
frame2.place(x=535,y=132)

frame3=Frame(root,height="140",width="191",bg="gray")
frame3.place(x=855,y=132)

frame4=Frame(root,height="140",width="191",bg="gray")
frame4.place(x=215,y=332)

frame5=Frame(root,height="140",width="191",bg="gray")
frame5.place(x=535,y=332)

#frame6=Frame(root,height="140",width="190",bg="gray")
#frame6.place(x=940,y=320)









#leftside

Frame2=Frame(root,height="800",width="210",bg="#363740")
Frame2.place(x=0,y=1)

cargo=Label(root, text="                                                         Cargo Management System                                                                                  ", font=('Rubik one', 22, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=0,y=2)

dashboard=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc")
dashboard.place(x=1,y=80)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white',
                    bd=0, cursor="hand2", activebackground="#e0dcdc",command=add_new_cargo)
<<<<<<< HEAD
addnewcargo.place(x=223,y=140)

Viewcargo=Button(root, text="View Cargo Details", font=("Herald", 13,"bold"),height=6,  width=17, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc",command=viewcargo)
Viewcargo.place(x=543,y=140)

Invoice_Details=Button(root, text="Invoice Details", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc",command=invoicedetails)
Invoice_Details.place(x=863,y=140)
=======
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc",)
Viewcargo.place(x=1,y=178)

cargotype=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)
>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f

employees=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
<<<<<<< HEAD
employees.place(x=223,y=340)
=======
employees.place(x=1,y=276)
>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f

Aboutus=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=about_us)
<<<<<<< HEAD
Aboutus.place(x=543,y=340)

#contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white', 
                # bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
#contactus.place(x=946,y=328)
=======
Aboutus.place(x=1,y=325)

contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contactus.place(x=1,y=374)
>>>>>>> 8dfc5beb3f47bde5783a5a8a7d97bca39201400f

Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=20, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1,y=423)


root.mainloop()