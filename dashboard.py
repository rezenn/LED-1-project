from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

def employee():
    root.destroy()
    import employee

def about_us():
    root.destroy()
    import about

def contact_us():
    root.destroy()
    import contact
#test function
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

bgimage = ImageTk.PhotoImage(file="dashboard.jpg")
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
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

#Frame2=Frame(root,height="800",width="210",bg="#363740")
#Frame2.place(x=0,y=1)

cargo=Label(root, text="Cargo Management System", font=('Rubik one', 10, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=28,y=2)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=6,  width=17, bg='#363740', fg='white',
                    bd=0, cursor="hand2", activebackground="#e0dcdc",command=add_new_cargo)
addnewcargo.place(x=308,y=128)

Viewcargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=6,  width=17, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc",)
Viewcargo.place(x=628,y=128)

cargotype=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=947,y=128)

employees=Button(root, text="Employee", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white', 
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
employees.place(x=308,y=328)

Aboutus=Button(root, text="About Us", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white',
                bd=0, cursor="hand2", activebackground="#e0dcdc",command=about_us)
Aboutus.place(x=626,y=328)

contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=6, width=17, bg='#363740', fg='white', 
                 bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contactus.place(x=946,y=328)

Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=15, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1000,y=700)


root.mainloop()