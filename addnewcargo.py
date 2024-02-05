from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')
root.iconbitmap("cargo_icon.ico")


#heading

Label1=Label(root, text="Add New Cargo", font=("Rubik one", 20))
Label1.place(x=265, y=30)



#frame

Frame1=Frame(root, height="590",width="900", bg="#e0dcdc")
Frame1.place(x=260, y=80)

#inside frame 1 sender

sender=Label(root, text="Sender", font=("Rubik one", 15, "bold"), bg=("#e0dcdc") )
sender.place(x=300, y=120)

namesender=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
namesender.place(x=300, y=170)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=395, y=170)


Addresssender=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Addresssender.place(x=300, y=200)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=395, y=200)


Pincodesender=Label(root, text="PIN Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodesender.place(x=300, y=230)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=395, y=230)


contactsender=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactsender.place(x=300, y=260)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=395, y=260)

    #inside frame 1 receiver

receiver=Label(root, text="Receiver", font=("Rubik one", 15, "bold"), bg=("#e0dcdc"))
receiver.place(x=730, y=120)


namereceiver=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
namereceiver.place(x=730, y=170)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=825, y=170)


Addressreceiver=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Addressreceiver.place(x=730, y=200)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=825, y=200)


Pincodereceiver=Label(root, text="PIN Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodereceiver.place(x=730, y=230)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=825, y=230)


contactreceiver=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactreceiver.place(x=730, y=260)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=825, y=260)


#middle Heading

cargoinfo=Label(root, text="                                  Cargo Information                                  ", font=("Rubik one", 23, "bold"))
cargoinfo.place(x=269, y=320)

#cargo type
lbl_cargotype=Label(root,text="Cargo Type: ",font=("Mulish",12) ,bg='#e0dcdc')
lbl_cargotype.place(x=300, y=400)

cargotype=Entry(root,  width=30, font=("Herald", 11))
cargotype.place(x=395, y=400)

#weight

weight=Label(root, text="Weight:", font=("Mulish",12) ,bg='#e0dcdc')
weight.place(x=300, y=430)

weightent=Entry(root, width=30, font=("Herald", 11))
weightent.place(x=395, y=430)

#Discription


discription=Label(root, text="Discription:", font=("Mulish",12) ,bg='#e0dcdc')
discription.place(x=730, y=400)

Discriptionent=Entry(root, width=30, font=("Herald", 11))
Discriptionent.place(x=825, y=400)

#frame 2 


Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

#image
logo=ImageTk.PhotoImage(file='logo.jpg')
bglabel=Label(root,image=logo)
bglabel.place(x=5,y=2)

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




root.mainloop()