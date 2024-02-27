from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as messagebox

def invoicedetails():
    root.destroy()
    import invoiceDetails


def viewcargo():
    root.destroy()
    import View_cargodetails

def add_new_cargo():
    root.destroy()
    import addnewcargo_emp    


def about_us():
    root.destroy()
    import about

def contact_us():
    root.destroy()
    import contact

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

Label1=Label(root, text="Contact Admin", font=("Rubik one", 20), bg="#faeded")
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

dashboard_button=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                         fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=dashboard)
dashboard_button.place(x=1,y=80)


add_new_cargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                    fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=add_new_cargo)
add_new_cargo.place(x=1,y=129)

View_cargo=Button(root, text="View Cargo Details", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=viewcargo)
View_cargo.place(x=1,y=178)
view_invoice_details=Button(root, text="View Invoice Details", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=invoicedetails)
view_invoice_details.place(x=1,y=227)
#employee_button=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', 
                #fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
#employee_button.place(x=1,y=276)

contact_admin=Button(root, text="Contact Admin", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contact_admin.place(x=1,y=276)
Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=22, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1,y=325)


#contact info

long_text="""
Our Branches

Greetings Cargo Global
 123 Shipping Lane
 Cityscape Central, Globalville
Contact Information:
 Phone: +1 (555) 123-4567
              +1 (555) 876-5432 
Email: info@greetingscargoglobal.com")


Greetings Cargo Global
789 Freight Avenue
 Metropolitan Hub, Worldport
Contact Information:
 Phone: +1 (555) 987-6543
              +1 (555) 234-5678
Email: info@greetingscargoglobal.com


Seamless Cargo Solutions
789 Express Lane
Metropolitan Plaza, Portside
Contact Information:
Phone: +1 (555) 789-0123
              +1 (555) 345-6789
Email: info@seamlesscargosolutions.com
"""
info=Label(root,text=long_text,font=("Herald",14),bg="#e0dcdc")
info.place(x=525,y=90)


root.mainloop()