from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as messagebox

def employee():
    root.destroy()
    import employee

def dashboard():
    root.destroy()
    import dashboard

def contact_us():
    root.destroy()
    import contact

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
root.title('Contact Us')
root.iconbitmap("cargo_icon.ico")

#heading

Label1=Label(root, text="About Us", font=("Rubik one", 20), bg="#faeded")
Label1.place(x=265, y=30)


#frame

Frame1=Frame(root, height="680",width="900", bg="#e0dcdc")
Frame1.place(x=260, y=80)


Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

#image
logo_img=ImageTk.PhotoImage(file="logo.jpg")
logo=Label(root,image=logo_img)
logo.place(x=5,y=2)

#Buttons

cargo=Label(root, text="Cargo Management System", font=('Herald', 11, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=32,y=6)
dashboard_button=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white',
                  bd=0, cursor="hand2", activebackground="#e0dcdc",command=dashboard)
dashboard_button.place(x=1,y=80)

add_new_cargo_button=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740',
                    fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=add_new_cargo)
add_new_cargo_button.place(x=1,y=129)

View_cargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
View_cargo.place(x=1,y=178)
cargo_type=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargo_type.place(x=1,y=227)

employees_button=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', 
                fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
employees_button.place(x=1,y=276)

About_us_button=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', 
               fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
About_us_button.place(x=1,y=325)

contact_us_button=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', 
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contact_us_button.place(x=1,y=374)




Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=22, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1,y=423)


#about us info

long_text="""
Greetings Cargo Global is a premier international logistics provider, excelling in facilitating 
the seamless exchange of goods through comprehensive support for land and air transport. 
Specializing in ocean freight, courier services, and import/export operations, Greetings
 Cargo Global ensures efficient cargo services to destinations worldwide, including
 Australia, Europe, Canada, the USA, and beyond. Our commitment to offering competitive 
 rates for air, land, and sea transportation positions us as a leader in the industry.

Established in 1970 by our visionary CEO, Mr. Samuel Anderson, who brings a decade of
expertise in logistics, Greetings Cargo Global has swiftly ascended the ranks by providing 
top-notch solutions for cargo transportation on both a national and international scale. 
Our central cargo office, strategically located in the heart of the city for accessibility, is
situated in downtown Globalville.

In addition to our transportation services, Greetings Cargo Global extends its capabilities 
to meet storage needs. With state-of-the-art warehouse facilities, we offer secure storage 
solutions, further enhancing our position as a comprehensive logistics provider. Leveraging 
our extensive global network, Greetings Cargo Global fulfills its commitment to being the 
premier logistics company globally.

""" 

info=Label(root,text=long_text,font=("Herald",16),bg="#e0dcdc")
info.place(x=290,y=130)


root.mainloop()