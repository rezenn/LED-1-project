from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.messagebox import askyesno, askquestion
import random
import string

def employee():
    root.destroy()
    import employee

def about_us():
    root.destroy()
    import about

def contact_us():
    root.destroy()
    import contact

def dashboard():
    root.destroy()
    import dashboard



root = tk.Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')
root.iconbitmap("cargo_icon.ico")



#heading

Label1=Label(root, text="Add New Cargo", font=("Rubik one", 20))
Label1.place(x=265, y=30)



#creating Variables

Sender_name=StringVar()
Sender_contact=StringVar()
receiver_name=StringVar()
receiver_contact=StringVar()
bill_num=StringVar()

R=random.randint(100,99999)
bill_num.set(R)


from_n=StringVar()
To_destination=StringVar()
rateperkg=IntVar()
weight=IntVar()
sub_total=StringVar()
tax_input=StringVar()
total=StringVar()




#frame

Frame1=Frame(root, height="670",width="930", bg="#e0dcdc")
Frame1.place(x=260, y=80)


tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=265,y=90,width=920,height=650)




#consignment number

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

consignment_id=Label(root, text="Consignment ID:", font=("Mulish", 12), bg="#e0dcdc")
consignment_id.place(x=300,y=123)


# Tkinter StringVar to store the generated consignment id
entry_var = tk.StringVar()

#Entry widget to display the consignment number
consignment_entry = tk.Entry(root, textvariable=entry_var, state='readonly', width=16, font=('Herald', 12))
consignment_entry.place(x=435,y=123)

# button to generate and display the consignment number
generate_button = tk.Button(root, text="Generate Consignment ID", font=("Herald", 9),cursor="hand2", command=generate_and_display_consignment)
generate_button.place(x=605,y=120)


#inside frame 1 sender

sender=Label(root, text="Sender", font=("Rubik one", 15, "bold"), bg=("#e0dcdc") )
sender.place(x=300, y=165)

namesender=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
namesender.place(x=300, y=215)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=435, y=215)


Addresssender=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Addresssender.place(x=300, y=250)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=435, y=250)


Pincodesender=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodesender.place(x=300, y=280)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=435, y=280)


contactsender=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactsender.place(x=300, y=310)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=435, y=310)





    #inside frame 1 receiver

receiver=Label(root, text="Receiver", font=("Rubik one", 15, "bold"), bg=("#e0dcdc"))
receiver.place(x=730, y=170)


namereceiver=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
namereceiver.place(x=730, y=220)

nameentry=Entry(root, width=30, font=("Herald", 11))
nameentry.place(x=865, y=220)


Addressreceiver=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Addressreceiver.place(x=730, y=250)

Addressentry=Entry(root, width=30, font=("Herald", 11))
Addressentry.place(x=865, y=250)


Pincodereceiver=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pincodereceiver.place(x=730, y=280)

Pincodeentry=Entry(root, width=30, font=("Herald", 11))
Pincodeentry.place(x=865, y=280)


contactreceiver=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contactreceiver.place(x=730, y=310)

contactentry=Entry(root, width=30, font=("Herald", 11))
contactentry.place(x=865, y=310)



#middle frame for fromto



from_toframe=Frame(root, height="55",width="880", relief=RIDGE, bd=9)
from_toframe.place(x=285,y=355)

Country=Label(root, text="From: ", font=("Mulish", 12) )
Country.place(x=300, y=370)

countryentry=ttk.Combobox(root,font=("arial",9,),width=12,state="readonly")
countryentry['value']=('Nepal')
countryentry.current(0)
countryentry.place(x=351, y=371)



countryre=Label(root,text="To: ",font=("Mulish",12) )
countryre.place(x=480, y=370)

combo_service=ttk.Combobox(root,font=("arial",9,),width=16,state="readonly")
combo_service['value']=('Select Destination' ,"United States", "Australia", "Thailand", "China", "United Kingdon", "Germany", "Finland", "France")
combo_service.current(0)
combo_service.place(x=515, y=371)

#weight

weight=Label(root, text="Weight (Kg): ", font=("Mulish",12))
weight.place(x=667, y=370)

weightent=Entry(root, width=10, font=("Herald", 11))
weightent.place(x=768, y=371)

#cargo type
lbl_cargotype=Label(root,text="Cargo Category: ",font=("Mulish",12))
lbl_cargotype.place(x=872, y=370)

combo_service=ttk.Combobox(root,font=("arial",9,),width=18,state="readwrite")
combo_service['value']=('Select Cargo Category' ,"Electronic Device", "Agricultural producr", "Veichles", "Medical Equipments", "Handicraft")
combo_service.current(0)
combo_service.place(x=1004, y=371)






#Invoice frame in frame 1


invoiceframe=Frame( bg="white")
invoiceframe.place(x=300, y=445,width=380, height=265)

scrooly=Scrollbar(invoiceframe,orient=VERTICAL)
textarea=Text(invoiceframe,yscrollcommand=scrooly.set, bg="white", fg="#1f1818", font=("Herald",9  ))
scrooly.pack(side=RIGHT, fill=Y)
scrooly.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)



#Invoice Heading

invoicel=Label(root, text="Invoice", font=("Gotham", 12, "bold"),bg=("#e0dcdc"))
invoicel.place(x=300, y=420)



#rateperkg

rateperkg=Label(root, text="Rate Per Kg:", font=("Mulish",12) ,bg='#e0dcdc')
rateperkg.place(x=730, y=425)

Discriptionent=Entry(root, width=30, font=("Herald", 11))
Discriptionent.place(x=865, y=425)

#Discription


discription=Label(root, text="Discription:", font=("Mulish",12) ,bg='#e0dcdc')
discription.place(x=730, y=455)

Discriptionent=Entry(root, width=30, font=("Herald", 11))
Discriptionent.place(x=865, y=455)


#subtotal


subtotalamt=Label(root, text="Sub Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
subtotalamt.place(x=730, y=485)

subtotalamtent=Entry(root,width=30, font=("Herald", 11) )
subtotalamtent.place(x=865, y=485)


#tax

govtax=Label(root, text="Gov Tax Nrs.", font=("Mulish", 12), bg="#e0dcdc")
govtax.place(x=730, y=515)

govtaxent=Entry(root,width=30, font=("Herald", 11) )
govtaxent.place(x=865, y=515)



#totalamount

totalamt=Label(root, text="Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
totalamt.place(x=730, y=545)

totalamtent=Entry(root,width=30, font=("Herald", 11) )
totalamtent.place(x=865, y=545)





total=Button(root, text="Total Amount", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
total.place(x=780,y=585)

Submit=Button(root, text="Submit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Submit.place(x=930,y=585)

Generatebill=Button(root, text="Generate Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Generatebill.place(x=780,y=635)

PrintInvoice=Button(root, text="Print Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
PrintInvoice.place(x=780,y=685)

SaveInvoice=Button(root, text="Save Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
SaveInvoice.place(x=930,y=635)

Exit=Button(root, command=root.destroy, text="Exit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Exit.place(x=930,y=685)


#frame 2 


Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

#image
logo=ImageTk.PhotoImage(file='logo.jpg')
bglabel=Label(root,image=logo)
bglabel.place(x=5,y=2)

cargo=Label(root, text="Cargo Management System", font=('Herald', 11, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=32,y=6)


dashboard_button=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                         fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=dashboard)
dashboard_button.place(x=1,y=80)

addnewcargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                    fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
addnewcargo.place(x=1,y=129)

Viewcargo=Button(root, text="View Cargo Details", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Viewcargo.place(x=1,y=178)

cargotype=Button(root, text="Cargo Status", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargotype.place(x=1,y=227)

employee_button=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', 
                fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
employee_button.place(x=1,y=276)

About_us_button=Button(root, text="About Us", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', 
               fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=about_us)
About_us_button.place(x=1,y=325)

contact_us_button=Button(root, text="Contact Us", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=contact_us)
contact_us_button.place(x=1,y=374)





#command fro logout

def log_out():
    msg_box = tk.messagebox.askquestion('Log out Application', 'Are you sure you want to exit the application?',
                                        icon='warning')
    if msg_box == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')



Logout=Button(root, text="Log Out", font=("Herald", 13,"bold"), command=log_out, height=2, width=22, bg='#363740', 
              fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Logout.place(x=1,y=423)




root.mainloop()