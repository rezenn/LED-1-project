from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.messagebox import askyesno, askquestion
from tkinter import messagebox
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



#creating Variables for entries

Sender_name=StringVar()
Sender_contact=StringVar()
receiver_name=StringVar()
receiver_contact=StringVar()
bill_num=StringVar()


R=random.randint(100,99999)
bill_num.set(R)


from_n=StringVar()
To_destination=StringVar()
rate_perkg=IntVar()
weight_in=IntVar()
sub_total=StringVar()
tax_input=StringVar()
total_with_tax=StringVar()
cargocatogary=StringVar()
entry_var=StringVar()


#creating Arrival Destination

destination=["Select Destination","United States", "Australia", "Thailand", "China", "United Kingdom", "Germany", "Finland", "France"]

rate_for_unitedstates=1070
rate_for_australia=900
rate_for_thailand=650
rate_for_china=610
rate_for_unitedkingdom=955
rate_for_germany=940
rate_for_finland=880
rate_for_france=910






#frame

Frame1=Frame(root, height="670",width="930", bg="#e0dcdc")
Frame1.place(x=260, y=80)


tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=265,y=90,width=920,height=650)








#consignment number generator part

def generate_consignment_number(length=10):
    
    if length < 2:
        raise ValueError("Length must be at least 2 to accommodate both letters and digits.")
    
    #Define characters (letters and digits) to choose from
    letters = string.ascii_uppercase
    digits = string.digits
    
    #Ensure unique letters and digits in the consignment number
    consignment_number = random.choice(letters) + random.choice(digits)
    
    #Randomly select the remaining characters
    remaining_characters = ''.join(random.choice(letters + digits) for _ in range(length - 2))
    
    #Shuffle the characters to ensure randomness
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

name_sender=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
name_sender.place(x=300, y=215)

name_entry=Entry(root, width=30,textvariable=Sender_name, font=("Herald", 11))
name_entry.place(x=435, y=215)


Address_sender=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Address_sender.place(x=300, y=250)

receiver_address_entry=Entry(root, width=30, font=("Herald", 11))
receiver_address_entry.place(x=435, y=250)


Pin_code_sender=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pin_code_sender.place(x=300, y=280)

Pin_code_sender_entry=Entry(root, width=30, font=("Herald", 11))
Pin_code_sender_entry.place(x=435, y=280)


contact_sender=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contact_sender.place(x=300, y=310)

sender_contact_entry=Entry(root, width=30,textvariable=Sender_contact, font=("Herald", 11))
sender_contact_entry.place(x=435, y=310)





    #inside frame 1 receiver

receiver=Label(root, text="Receiver", font=("Rubik one", 15, "bold"), bg=("#e0dcdc"))
receiver.place(x=730, y=170)


name_receiver=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
name_receiver.place(x=730, y=220)

receiver_name_entry=Entry(root,textvariable=receiver_name, width=30, font=("Herald", 11))
receiver_name_entry.place(x=865, y=220)


Address_receiver=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Address_receiver.place(x=730, y=250)

receiver_address_entry=Entry(root, width=30, font=("Herald", 11))
receiver_address_entry.place(x=865, y=250)


Pin_code_receiver=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pin_code_receiver.place(x=730, y=280)

Pin_code_reciever_entry=Entry(root, width=30, font=("Herald", 11))
Pin_code_reciever_entry.place(x=865, y=280)


contact_receiver=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contact_receiver.place(x=730, y=310)

sender_contact_entry=Entry(root,textvariable=receiver_contact, width=30, font=("Herald", 11))
sender_contact_entry.place(x=865, y=310)



#middle frame for fromto



from_to_frame=Frame(root, height="55",width="880", relief=RIDGE, bd=9)
from_to_frame.place(x=285,y=355)

Country=Label(root, text="From: ", font=("Mulish", 12) )
Country.place(x=300, y=370)

country_entry=ttk.Combobox(root,font=("arial",9,),width=12,state="readonly", textvariable=from_n)
country_entry['value']=('Nepal')
country_entry.current(0)
country_entry.place(x=351, y=371)


#for rate per kg

def rateforkg(event=""):
      if combo_destination.get()=="United States":
        rateperkgent.config(value=rate_for_unitedstates)
        rateperkgent.current(0)
        weight_in.set(1)


      if combo_destination.get()=="Australia":
        rateperkgent.config(value=rate_for_australia)
        rateperkgent.current(0)
        weight_in.set(1)

      if combo_destination.get()=="Thailand":
        rateperkgent.config(value=rate_for_thailand)
        rateperkgent.current(0)
        weight_in.set(1)

      if combo_destination.get()=="China":
        rateperkgent.config(value=rate_for_china)
        rateperkgent.current(0)
        weight_in.set(1)  

      if combo_destination.get()=="United Kingdom":
        rateperkgent.config(value=rate_for_unitedkingdom)
        rateperkgent.current(0)
        weight_in.set(1)  

      if combo_destination.get()=="Germany":
        rateperkgent.config(value=rate_for_germany)
        rateperkgent.current(0)
        weight_in.set(1)  

      if combo_destination.get()=="Finland":
        rateperkgent.config(value=rate_for_finland)
        rateperkgent.current(0)
        weight_in.set(1)  

      if combo_destination.get()=="France":
        rateperkgent.config(value=rate_for_france)
        rateperkgent.current(0)
        weight_in.set(1)  

             


countryre=Label(root,text="To: ",font=("Mulish",12) )
countryre.place(x=480, y=370)

combo_destination=ttk.Combobox(root,value=[""],font=("arial",9,),values=destination,width=16,state="readonly",textvariable=To_destination)

combo_destination.place(x=515, y=371)
combo_destination.current(0)
combo_destination.bind("<<ComboboxSelected>>", rateforkg)

#rateperkg

rateperkg=Label(root, text="Rate Per Kg:", font=("Mulish",12) ,bg='#e0dcdc')
rateperkg.place(x=730, y=425)

rateperkgent=ttk.Combobox(root, width=25,state="readonly",textvariable=rate_perkg, font=("Herald", 11))
rateperkgent.place(x=865, y=425)

#weight

weight=Label(root, text="Weight (Kg): ", font=("Mulish",12))
weight.place(x=667, y=370)

weightent=Entry(root, width=10, font=("Herald", 11),textvariable=weight_in)
weightent.place(x=768, y=371)

#cargo type
lbl_cargotype=Label(root,text="Cargo Category: ",font=("Mulish",12))
lbl_cargotype.place(x=872, y=370)

combo_service=ttk.Combobox(root,font=("arial",9,),width=18,state="readwrite",textvariable=cargocatogary)
combo_service['value']=('Select Cargo Category' ,"Electronic Device", "Agricultural producr", "Veichles", "Medical Equipments", "Handicraft")
combo_service.current(0)
combo_service.place(x=1004, y=371)

#Invoice frame in frame 

invoiceframe=Frame( bg="white")
invoiceframe.place(x=300, y=445,width=380, height=265)

scrooly=Scrollbar(invoiceframe,orient=VERTICAL)
textarea=Text(invoiceframe,yscrollcommand=scrooly.set, bg="white", fg="#1f1818", font=("Herald",9  ))
scrooly.pack(side=RIGHT, fill=Y)
scrooly.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)


#========Declearing the functionsfor 

def first_view():
        textarea.delete(1.0,END)
        textarea.insert(END,"\t             CARGO MANAGEMENT SYSTEM                               ")

        textarea.insert(END,f"\n Bill Number: {bill_num.get()}")
        textarea.insert(END,f"\n Consignment ID: ")
        textarea.insert(END,f"\n Client Name: ")
        textarea.insert(END,f"\n Client Contect: ")
        textarea.insert(END,"\n-----------------------------------------------------------------------------------------")
        textarea.insert(END, f"\n Cargo Destination\t\t\tWeight\t\tRate Per Kg")
        textarea.insert(END,"\n-----------------------------------------------------------------------------------------")

first_view()




def totalaftertax():
   n=rate_perkg.get()
   m=weight_in.get()*n
   
  
   if To_destination.get()=="Select Destination":
      messagebox.showerror("Error", "Please Select The Cargo Destination" )
      
   else:
      
      textarea.delete(1.0,END)
      textarea.insert(END,"\t             CARGO MANAGEMENT SYSTEM                               ")

      textarea.insert(END,f"\n Bill Number:{bill_num.get()}")
      textarea.insert(END,f"\n Consignment ID:{entry_var.get()}")
      textarea.insert(END,f"\n Client Name:{Sender_name.get()}")
      textarea.insert(END,f"\n Client Contect:{Sender_contact.get()}")
      textarea.insert(END,"\n-----------------------------------------------------------------------------------------")
      textarea.insert(END, f"\n Cargo Destination\t\t\tWeight\t\tRate Per Kg")
      textarea.insert(END,"\n-----------------------------------------------------------------------------------------")





      textarea.insert(END,f"\n {To_destination.get()}\t\t\t{weight_in.get()}\t\t{rate_perkg.get()}")
      textarea.insert(END,f"\n                                                                    ")
      textarea.insert(END,f"\n                                                                    ")

  

      
      sub_total.set(str(m))
      tax_input.set(str(0.05*m))
      total_with_tax.set(str(m+(0.05*m)))



      textarea.insert(END,f"\n \t\t\tSub Total:Rs.  {sub_total.get()} ")
      textarea.insert(END,f"\n \t\t\tGov Tax 5(%):Rs.  {tax_input.get()} ")
      textarea.insert(END,f"\n \t\t\tTotal:Rs.  {total_with_tax.get()} ")

#Invoice Heading

invoicel=Label(root, text="Invoice", font=("Gotham", 12, "bold"),bg=("#e0dcdc"))
invoicel.place(x=300, y=420)

#Discription

discription=Label(root, text="Discription:", font=("Mulish",12) ,bg='#e0dcdc')
discription.place(x=730, y=455)

Discriptionent=Entry(root, width=30, font=("Herald", 11))
Discriptionent.place(x=865, y=455)


#subtotal


subtotalamt=Label(root, text="Sub Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
subtotalamt.place(x=730, y=485)

subtotalamtent=Entry(root,width=30, font=("Herald", 11), textvariable=sub_total )
subtotalamtent.place(x=865, y=485)


#tax

govtax=Label(root, text="Gov Tax Nrs.", font=("Mulish", 12), bg="#e0dcdc")
govtax.place(x=730, y=515)

govtaxent=Entry(root,width=30, font=("Herald", 11), textvariable=tax_input )
govtaxent.place(x=865, y=515)

#totalamount

totalamt=Label(root, text="Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
totalamt.place(x=730, y=545)

totalamtent=Entry(root,width=30, font=("Herald", 11), textvariable=total_with_tax)
totalamtent.place(x=865, y=545)

total=Button(root, text="Total Amount", command=totalaftertax, font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
total.place(x=780,y=585)

Submit=Button(root, text="Submit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Submit.place(x=930,y=585)


PrintInvoice=Button(root, text="Print Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
PrintInvoice.place(x=780,y=635)

SaveInvoice=Button(root, text="Save Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
SaveInvoice.place(x=930,y=635)

Exit=Button(root, command=root.destroy, text="Exit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Exit.place(x=855,y=685)


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