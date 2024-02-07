from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import random
import string


root = tk.Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')
root.iconbitmap("cargo_icon.ico")

def generate_consignment_number(length=10):
    # Ensure the length is at least 2 to accommodate both letters and digits
    if length < 2:
        raise ValueError("Length must be at least 2 to accommodate both letters and digits.")
    
    # Define the pool of characters (letters and digits) to choose from
    letters = string.ascii_uppercase
    digits = string.digits
    
    # Ensure unique letters and digits in the consignment number
    consignment_number = random.choice(letters) + random.choice(digits)
    
    # Randomly select the remaining characters
    remaining_characters = ''.join(random.choice(letters + digits) for _ in range(length - 2))
    
    # Shuffle the characters to ensure randomness
    consignment_number += ''.join(random.sample(remaining_characters, len(remaining_characters)))
    
    return consignment_number

def generate_and_display_consignment():
    consignment_number = generate_consignment_number()
    entry_var.set(consignment_number)


#heading

Label1=Label(root, text="Add New Cargo", font=("Rubik one", 20))
Label1.place(x=265, y=30)



#frame

Frame1=Frame(root, height="670",width="930", bg="#e0dcdc")
Frame1.place(x=260, y=80)


tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=265,y=90,width=920,height=650)


#inside frame 1 sender

sender=Label(root, text="Sender", font=("Rubik one", 15, "bold"), bg=("#e0dcdc") )
sender.place(x=300, y=120)

namesender=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
namesender.place(x=300, y=170)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=435, y=170)


Addresssender=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Addresssender.place(x=300, y=200)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=435, y=200)


Pincodesender=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodesender.place(x=300, y=230)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=435, y=230)


contactsender=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactsender.place(x=300, y=260)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=435, y=260)

Country=Label(root, text="Country:", font=("Mulish", 12), bg="#e0dcdc" )
Country.place(x=300, y=290)

countryentry=ttk.Combobox(root,font=("arial",9,),width=18,state="readonly")
countryentry['value']=('Nepal')
countryentry.current(0)
countryentry.place(x=435, y=290)



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


Pincodereceiver=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodereceiver.place(x=730, y=230)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=825, y=230)


contactreceiver=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactreceiver.place(x=730, y=260)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=825, y=260)


countryre=Label(root,text="Country: ",font=("Mulish",12) ,bg='#e0dcdc')
countryre.place(x=730, y=290)

combo_service=ttk.Combobox(root,font=("arial",9,),width=22,state="readwrite")
combo_service['value']=('Select Destination' ,"United States", "Australia", "Thailand", "China", "United Kingdon", "Germany", "Finland", "France")
combo_service.current(0)
combo_service.place(x=825, y=290)




#middle Heading

cargoinfo=Label(root, text="                                  Cargo Information                                  ", font=("Rubik one", 23, "bold"))
cargoinfo.place(x=285, y=330)

#consignment number

consignment_id=Label(root, text="Consignment ID:", font=("Mulish", 12), bg="#e0dcdc")
consignment_id.place(x=300,y=400)


# Tkinter StringVar to store the generated consignment id
entry_var = tk.StringVar()

#Entry widget to display the consignment number
consignment_entry = tk.Entry(root, textvariable=entry_var, state='readonly', width=16, font=('Herald', 16))
consignment_entry.place(x=435,y=395)

# button to generate and display the consignment number
generate_button = tk.Button(root, text="Generate Consignment ID", font=("Herald", 10), command=generate_and_display_consignment)
generate_button.place(x=435,y=430)



#cargo type
lbl_cargotype=Label(root,text="Cargo Catagory: ",font=("Mulish",12) ,bg='#e0dcdc')
lbl_cargotype.place(x=300, y=465)

combo_service=ttk.Combobox(root,font=("arial",9,),width=22,state="readwrite")
combo_service['value']=('Select Cargo Catagory' ,"Electronic Device", "Agricultural producr", "Veichles", "Medical Equipments", "Handicraft")
combo_service.current(0)
combo_service.place(x=435, y=465)


#ratelist frame in frame 1


rateframe=Frame(width=200, height=300, bg="white")
rateframe.place(x=850, y=400)


#Discription


discription=Label(root, text="Discription:", font=("Mulish",12) ,bg='#e0dcdc')
discription.place(x=300, y=495)

Discriptionent=Entry(root, width=30, font=("Herald", 11))
Discriptionent.place(x=435, y=495)



RatePerKg=Label(root, text="Rate/Kg: ", font=("Mulish",12) ,bg='#e0dcdc') 
RatePerKg.place(x=300, y=525)

RatePerKgent=Entry(root,width=30, font=("Herald", 11) )
RatePerKgent.place(x=435, y=525)


#weight

weight=Label(root, text="Weight:", font=("Mulish",12) ,bg='#e0dcdc')
weight.place(x=300, y=555)

weightent=Entry(root, width=30, font=("Herald", 11))
weightent.place(x=435, y=555)


#totalamount

totalamt=Label(root, text="Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
totalamt.place(x=300, y=585)

totalamtent=Entry(root,width=30, font=("Herald", 11) )
totalamtent.place(x=435, y=585)







Submit=Button(root, text="Submit", font=("Herald", 13,"bold"), height=2, width=12, bg='#8E8EBC', fg='black', bd=0, cursor="hand2", activebackground="#e0dcdc")
Submit.place(x=300,y=640)



#frame 2 


Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

#image
logo=ImageTk.PhotoImage(file='logo.jpg')
bglabel=Label(root,image=logo)
bglabel.place(x=5,y=2)

cargo=Label(root, text="Cargo Management System", font=('Herald', 11, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=32,y=6)


dashboard=Button(root, text="Dashboard            ", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
dashboard.place(x=1,y=80)

addnewcargo=Button(root, text="  Add New Cargo       ", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="       View Cargo Details       ", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Viewcargo.place(x=1,y=178)

cargotype=Button(root, text="Cargo Status        ", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)

employee=Button(root, text="Employee              ", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
employee.place(x=1,y=276)

Aboutus=Button(root, text="About Us              ", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Aboutus.place(x=1,y=325)

contactus=Button(root, text="Contact Us           ", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
contactus.place(x=1,y=374)




root.mainloop()