from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.messagebox import askyesno, askquestion
from tkinter import messagebox
import random
import string
<<<<<<< HEAD
import random, os
import mysql.connector as mysql
=======
import random,os
>>>>>>> 1a00011e654948e683d633433d969019dfd9a494

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

def create():
    # get data typed by the user
    consignment_id = consignment_entry.get()
    sender_name = name_sender_entry.get()
    sender_address = sender_address_entry.get()
    sender_contact = sender_contact_entry.get()
    sender_pin_code = Pin_code_sender_entry.get()
    receiver_name = receiver_name_entry.get()
    receiver_address = receiver_address_entry.get()
    receiver_contact = receiver_contact_entry.get()
    receiver_pin_code = Pin_code_reciever_entry.get()
    from_country = from_country_entry.get()
    to_country = combo_destination.get()
    weight = weight_entry.get()
    rate_per_kg = rate_per_kg_entry.get()
    cargo_category = combo_service.get()
    bill = bill_entry.get()
    sub_total_db = sub_total_amt_entry.get()
    gov_tax_db = gov_tax_entry.get()
    total_amt_db = total_amt_entry.get()

    # show error if the instructions are not followed
    if consignment_id == "" or sender_name == "" or sender_contact == "" or sender_address == "" or sender_pin_code == "":
        messagebox.showinfo("ALERT", "Enter every component !!!")
    elif receiver_name == "" or receiver_address == "" or receiver_contact == "" or receiver_address == "" or receiver_pin_code == "":
        messagebox.showinfo("ALERT", "Enter every component !!!")
    elif from_country == "" or to_country == "" or receiver_contact == "" or weight == "" or rate_per_kg == "" or cargo_category == "":
        messagebox.showinfo("ALERT", "Enter every component !!!")
    elif receiver_name == "" or bill == "" or sub_total_db == "" or gov_tax_db == "" or total_amt_db == "":
        messagebox.showinfo("ALERT", "Enter every component !!!")
    else:
        con = mysql.connect(
            host="localhost", 
            user="root",
            password="root",
            database="cargo_mngt"
        )
        cursor = con.cursor()

<<<<<<< HEAD
        # Insert the data into the database
        try:
            cursor.execute(
                "INSERT INTO cargos (consignment_id, sender_full_name, sender_address, sender_zip_code, sender_contact, receiver_full_name, receiver_address, receiver_zip_code, receiver_contact, from_destination, to_destination, weight, cargo_category, invoice_id, rate_per_kg, sub_total, gov_tax, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (consignment_id, sender_name, sender_address, sender_pin_code, sender_contact, receiver_name, receiver_address, receiver_pin_code, receiver_contact, from_country, to_country, weight, cargo_category, bill, rate_per_kg, sub_total_db, gov_tax_db, total_amt_db)
            )
            con.commit()
            messagebox.showinfo("Status", "Successfully registered")
        except mysql.Error as e:
            print(f"Error: {e}")
            con.rollback()
        finally:
           con.close()
=======
>>>>>>> 1a00011e654948e683d633433d969019dfd9a494


root = tk.Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')
root.iconbitmap("cargo_icon.ico")
#heading
Label1=Label(root, text="Add New Cargo", font=("Rubik one", 20))
Label1.place(x=265, y=30)
<<<<<<< HEAD
#creating Variables for entries
=======



#creating Variables for   ssdeentries

>>>>>>> 1a00011e654948e683d633433d969019dfd9a494
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
name_sender_entry=Entry(root, width=30,textvariable=Sender_name, font=("Herald", 11))
name_sender_entry.place(x=435, y=215)
Address_sender_label=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Address_sender_label.place(x=300, y=250)
sender_address_entry=Entry(root, width=30, font=("Herald", 11))
sender_address_entry.place(x=435, y=250)
Pin_code_sender_label=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pin_code_sender_label.place(x=300, y=280)
Pin_code_sender_entry=Entry(root, width=30, font=("Herald", 11))
Pin_code_sender_entry.place(x=435, y=280)
contact_sender_label=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contact_sender_label.place(x=300, y=310)
sender_contact_entry=Entry(root, width=30,textvariable=Sender_contact, font=("Herald", 11))
sender_contact_entry.place(x=435, y=310)
    #inside frame 1 receiver
receiver=Label(root, text="Receiver", font=("Rubik one", 15, "bold"), bg=("#e0dcdc"))
receiver.place(x=730, y=170)
name_receiver_label=Label(root, text="Full Name:", font=("Mulish", 12 ), bg=('#e0dcdc'))
name_receiver_label.place(x=730, y=220)
receiver_name_entry=Entry(root,textvariable=receiver_name, width=30, font=("Herald", 11))
receiver_name_entry.place(x=865, y=220)
Address_receiver_label=Label(root, text="Address:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Address_receiver_label.place(x=730, y=250)
receiver_address_entry=Entry(root, width=30, font=("Herald", 11))
receiver_address_entry.place(x=865, y=250)
Pin_code_receiver_label=Label(root, text="ZIP Code:", font=("Mulish", 12 ), bg=('#e0dcdc'))
Pin_code_receiver_label.place(x=730, y=280)
Pin_code_reciever_entry=Entry(root, width=30, font=("Herald", 11))
Pin_code_reciever_entry.place(x=865, y=280)
contact_receiver_label=Label(root, text="Contact:", font=("Mulish", 12 ), bg=('#e0dcdc'))
contact_receiver_label.place(x=730, y=310)
receiver_contact_entry=Entry(root,textvariable=receiver_contact, width=30, font=("Herald", 11))
receiver_contact_entry.place(x=865, y=310)
#middle frame for fromto
from_toframe=Frame(root, height="55",width="880", relief=RIDGE, bd=9)
from_toframe.place(x=285,y=355)
from_country_label=Label(root, text="From: ", font=("Mulish", 12) )
from_country_label.place(x=300, y=370)
from_country_entry=ttk.Combobox(root,font=("arial",9,),width=12,state="readonly", textvariable=from_n)
from_country_entry['value']=('Nepal')
from_country_entry.current(0)
from_country_entry.place(x=351, y=371)
#for rate per kg
def rateforkg(event=""):
      if combo_destination.get()=="United States":
        rate_per_kg_entry.config(value=rate_for_unitedstates)
        rate_per_kg_entry.current(0)
        weight_in.set(1)
      if combo_destination.get()=="Australia":
        rate_per_kg_entry.config(value=rate_for_australia)
        rate_per_kg_entry.current(0)
        weight_in.set(1)
      if combo_destination.get()=="Thailand":
        rate_per_kg_entry.config(value=rate_for_thailand)
        rate_per_kg_entry.current(0)
        weight_in.set(1)
      if combo_destination.get()=="China":
        rate_per_kg_entry.config(value=rate_for_china)
        rate_per_kg_entry.current(0)
        weight_in.set(1)  
      if combo_destination.get()=="United Kingdom":
        rate_per_kg_entry.config(value=rate_for_unitedkingdom)
        rate_per_kg_entry.current(0)
        weight_in.set(1)  
      if combo_destination.get()=="Germany":
        rate_per_kg_entry.config(value=rate_for_germany)
        rate_per_kg_entry.current(0)
        weight_in.set(1)  
      if combo_destination.get()=="Finland":
        rate_per_kg_entry.config(value=rate_for_finland)
        rate_per_kg_entry.current(0)
        weight_in.set(1)  
      if combo_destination.get()=="France":
        rate_per_kg_entry.config(value=rate_for_france)
        rate_per_kg_entry.current(0)
        weight_in.set(1)  
             
to_country_label=Label(root,text="To: ",font=("Mulish",12) )
to_country_label.place(x=480, y=370)
combo_destination=ttk.Combobox(root,value=[""],font=("arial",9,),values=destination,width=16,state="readonly",textvariable=To_destination)
combo_destination.place(x=515, y=371)
combo_destination.current(0)
combo_destination.bind("<<ComboboxSelected>>", rateforkg)
#rateperkg
rate_per_kg_label=Label(root, text="Rate Per Kg:", font=("Mulish",12) ,bg='#e0dcdc')
rate_per_kg_label.place(x=730, y=425)
rate_per_kg_entry=ttk.Combobox(root, width=25,state="readonly",textvariable=rate_perkg, font=("Herald", 11))
rate_per_kg_entry.place(x=865, y=425)
#weight
weight_label=Label(root, text="Weight (Kg): ", font=("Mulish",12))
weight_label.place(x=667, y=370)
weight_entry=Entry(root, width=10, font=("Herald", 11),textvariable=weight_in)
weight_entry.place(x=768, y=371)
#cargo type
lbl_cargotype=Label(root,text="Cargo Category: ",font=("Mulish",12))
lbl_cargotype.place(x=872, y=370)
combo_service=ttk.Combobox(root,font=("arial",9,),width=18,state="readwrite",textvariable=cargocatogary)
combo_service['value']=('Select Cargo Category' ,"Electronic Device", "Agricultural product", "Veichles", "Medical Equipments", "Handicraft")
combo_service.current(0)
combo_service.place(x=1004, y=371)
#Invoice frame in frame 1
#INvoice
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
invoice_label=Label(root, text="Invoice", font=("Gotham", 12, "bold"),bg=("#e0dcdc"))
invoice_label.place(x=300, y=420)



<<<<<<< HEAD
#Discription
#Billnumber


bill_label=Label(root, text="Bill Number:", font=("Mulish",12) ,bg='#e0dcdc')
bill_label.place(x=730, y=455)

bill_entry=Entry(root, width=30, font=("Herald", 11), state="readonly",textvariable=bill_num )
bill_entry.place(x=865, y=455)
=======
#Billnumber


billlabel=Label(root, text="Bill Number:", font=("Mulish",12) ,bg='#e0dcdc')
billlabel.place(x=730, y=455)

billentry=Entry(root, width=30, font=("Herald", 11), state="readonly",textvariable=bill_num )
billentry.place(x=865, y=455)
>>>>>>> 1a00011e654948e683d633433d969019dfd9a494


#subtotal
sub_total_amt=Label(root, text="Sub Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
sub_total_amt.place(x=730, y=485)
sub_total_amt_entry=Entry(root,width=30, font=("Herald", 11), textvariable=sub_total )
sub_total_amt_entry.place(x=865, y=485)
#tax
gov_tax=Label(root, text="Gov Tax Nrs.", font=("Mulish", 12), bg="#e0dcdc")
gov_tax.place(x=730, y=515)
gov_tax_entry=Entry(root,width=30, font=("Herald", 11), textvariable=tax_input )
gov_tax_entry.place(x=865, y=515)
#totalamount
total_amt=Label(root, text="Total Nrs.", font=("Mulish", 12), bg="#e0dcdc")
total_amt.place(x=730, y=545)
total_amt_entry=Entry(root,width=30, font=("Herald", 11), textvariable=total_with_tax)
total_amt_entry.place(x=865, y=545)



#buttons


<<<<<<< HEAD

total=Button(root, text="Total Amount", command=totalaftertax, font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
total=Button(root, text="Total Amount", command=totalaftertax, font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc")
total.place(x=780,y=585)

Submit=Button(root, text="Submit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
=======
total=Button(root, text="Total Amount", command=totalaftertax, font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc")
total.place(x=780,y=585)

>>>>>>> 1a00011e654948e683d633433d969019dfd9a494
Submit=Button(root, text="Submit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc")
Submit.place(x=930,y=585)


<<<<<<< HEAD
Print_invoice=Button(root, text="Print Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Print_invoice.place(x=780,y=635)

def save_invoice():
   op=messagebox.askyesno("Save Invoice", "Do you want to save the Bill")
   if op>0:
      invoice_data=textarea.get(1.0,END)
      f1=open("Invoice/"+str(bill_num.get())+".txt",'w')
      f1.write(invoice_data)
      op=messagebox.askyesno("Saved", f"Bill No:{ bill_num.get()} saved successfully")
      f1.close()

Save_data=Button(root, text="Save Data", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=create)
Save_data.place(x=930,y=635)

Exit=Button(root, command=root.destroy, text="Exit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
Exit.place(x=855,y=685)
Save_invoice=Button(root, text="Save Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc", command=save_invoice)
Save_invoice.place(x=780,y=635)

=======
#PrintInvoice=Button(root, text="Print Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc")
#PrintInvoice.place(x=780,y=635)



def save_invoice():
   op=messagebox.askyesno("Save Invoice", "Do you want to save the Bill")
   if op>0:
      invoice_data=textarea.get(1.0,END)
      f1=open("Invoice/"+str(bill_num.get())+".txt",'w')
      f1.write(invoice_data)
      op=messagebox.askyesno("Saved", f"Bill No:{ bill_num.get()} saved successfully")
      f1.close()

SaveInvoice=Button(root, text="Save Invoice", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc", command=save_invoice)
SaveInvoice.place(x=780,y=635)

Exit=Button(root, command=root.destroy, text="Exit", font=("Herald", 12,"bold"), height=1, width=13, bg='#8E8EBC', fg='white', cursor="hand2", activebackground="#e0dcdc")
Exit.place(x=930,y=635)
>>>>>>> 1a00011e654948e683d633433d969019dfd9a494


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
add_new_cargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                    fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
add_new_cargo.place(x=1,y=129)
View_cargo=Button(root, text="View Cargo Details", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
View_cargo.place(x=1,y=178)
cargo_type=Button(root, text="Cargo Status", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc")
cargo_type.place(x=1,y=227)
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
# ... (Rest of your code)

<<<<<<< HEAD
root.mainloop()
=======



root.mainloop()
>>>>>>> 1a00011e654948e683d633433d969019dfd9a494
