from tkinter import *
from PIL import ImageTk

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Contact Us')
root.iconbitmap("cargo_icon.ico")

#heading

Label1=Label(root, text="Contact Us", font=("Rubik one", 20), bg="#faeded")
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