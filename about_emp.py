from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as messagebox

def dashboard():
    root.destroy()
    import employeedashboard


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

cargo=Label(root, text="                                                         Cargo Management System                                                                                  ", font=('Rubik one', 22, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=0,y=2)


#Buttons

Label1=Label(root,text="About Us",font=("Rubik one",20),bg="#Faeded")
Label1.place(x=195,y=53)



#frame
Frame1=Frame(root, height="585",width="930", bg="#e0dcdc")
Frame1.place(x=165, y=100)
tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=169,y=100,width=920,height=580)

back=Button(root, text="Back", font=("Herald", 13,"bold"), command=dashboard, height=2, width=15, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
back.place(x=800,y=700)

Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=15, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1000,y=700)

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
info.place(x=205,y=130)


root.mainloop()