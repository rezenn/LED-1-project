from tkinter import *
from PIL import ImageTk

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
dashboard=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
dashboard.place(x=1,y=80)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="View Cargo", font=("Herald", 13,"bold"),height=2,  width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Viewcargo.place(x=1,y=178)
cargotype=Button(root, text="Cargo Type", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)

employee=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
employee.place(x=1,y=276)

Aboutus=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Aboutus.place(x=1,y=325)

contactus=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=20, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
contactus.place(x=1,y=374)

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