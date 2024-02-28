from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import askyesno, askquestion
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


def view_invoice_details():
    root.destroy()
    import view_invoice_details


def employee():
    root.destroy()
    import employees

def about_us():
    root.destroy()
    import about

def viewcargo():
    root.destroy()
    import view_cargo_details
#test function
def add_new_cargo():
    root.destroy()
    import addnewcargo
def dashboard():
    root.destroy()
    import dashboard

root = tk.Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('View Cargo Details')
root.iconbitmap("cargo_icon.ico")

def search_button():
    search_value = consignment_entry.get()
    if not search_value:
        messagebox.showerror("Error", "Please enter a search value.")
        return

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()

    try:
        # Execute SQL query to search for data
        cursor.execute("SELECT * FROM cargos WHERE Consignment_ID = %s", (search_value,))
        rows = cursor.fetchall()

        if not rows:
            messagebox.showinfo("No Results", "No matching records found.")
        else:
            # Clear existing data in the table
            for row in Details_table.get_children():
                Details_table.delete(row)

            # Insert the fetched rows into the table
            for row in rows:
                Details_table.insert('', 'end', values=row)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    
    for row in Details_table.get_children():
        Details_table.delete(row)

    # Insert the fetched rows into the table
    for row in rows:
        Details_table.insert('', 'end', values=(row[1], row[11], row[2], row[5], row[6], row[9], row[8], row[18], row[12], row[13]))
    
    conn.close()

def addnew_cargo():
    root.destroy()
    import addnewcargo

def display_cargo():
    print("Displaying Cargo Info...")
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cargos")
    rows = cursor.fetchall()
#uuk
    # Clear existing data in the table
    for row in Details_table.get_children():
        Details_table.delete(row)

    # Insert the fetched rows into the table
    for row in rows:
        Details_table.insert('', 'end', values=(row[1], row[11], row[2], row[5], row[6], row[9], row[8], row[18], row[12], row[13]))
    conn.close()

def delete_cargo_details():
    selected_item = Details_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an cargo to delete.")
        return
    
    for item in selected_item:
        # Get the cargo id from the selected item
        consignment_id = Details_table.item(item, 'values')[0]

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()

    # Execute the SQL query to delete the selected employee
    cursor.execute("DELETE FROM cargos WHERE consignment_id = %s", (consignment_id,))
    conn.commit()
    messagebox.showinfo("Status", "cargo deleted successfully")

    conn.close()
    Details_table.delete(selected_item)




#heading

Label1=Label(root, text="View Cargo Details", font=("Rubik one", 20))
Label1.place(x=265, y=30)




#frame

Frame1=Frame(root, height="670",width="930", bg="#e0dcdc")
Frame1.place(x=260, y=80)


boldframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
boldframe.place(x=265,y=90,width=920,height=650)








consignment_id=Label(root, text="Consignment ID:", font=("Mulish", 12), bg="#e0dcdc")
consignment_id.place(x=300,y=123)

consignment_entry = tk.Entry(root, width=16, font=('Herald', 12))
consignment_entry.place(x=435,y=123)

Search_button = tk.Button(root, text="  Search  ", font=("Herald", 9),cursor="hand2", command=search_button)
Search_button.place(x=605,y=120)

#+++++++++++cargodetailstable==================

#tableframe

table_frame=Frame(root,bd=1,relief=RIDGE)
table_frame.place(x=282, y=170, width=888, height=490)

scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

Details_table=ttk.Treeview(table_frame,column=('Consignment ID','Cargo Destination', 'Sender', 'S.Contact', 'Receiver', 'R.contact', 'R.Zip Code', 'Total' , 'Weight', 'Category'), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=Details_table.xview)
scroll_y.config(command=Details_table.yview)

Details_table.heading('Consignment ID', text='Consignment ID')
Details_table.heading('Cargo Destination', text='Cargo Destination')
Details_table.heading('Sender', text='Sender Name')
Details_table.heading('S.Contact', text='Sender Contact')
Details_table.heading('Receiver', text='Receiver Name')
Details_table.heading('R.contact', text='Receiver Contact')
Details_table.heading('R.Zip Code', text='R.Zip Code')
Details_table.heading('Total', text='Total')
Details_table.heading('Weight', text='Weight')
Details_table.heading('Category', text='Category')

Details_table['show']='headings'

Details_table.column("Consignment ID",width=100)
Details_table.column("Cargo Destination",width=102)
Details_table.column("Sender",width=100)
Details_table.column("S.Contact",width=100)
Details_table.column("Receiver",width=100)
Details_table.column("R.contact",width=100)
Details_table.column("R.Zip Code",width=100)
Details_table.column("Total",width=100)
Details_table.column("Weight",width=100)
Details_table.column("Category",width=130)



Details_table.pack(fill=BOTH,expand=1)






# Button
add=Button(root, text="Add", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=9 , height=1, command=addnew_cargo)
add.place(x=550, y=670)



delete=Button(root, text="Delete", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=9 , height=1, command=delete_cargo_details)
delete.place(x=750, y=670)











#Invoice frame in frame 1

















#frame 2 


Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)

#image
logo=ImageTk.PhotoImage(file='logo.jpg')
bglabel=Label(root,image=logo)
bglabel.place(x=5,y=2)
dashboard_button=Button(root, text="Dashboard", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                         fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=dashboard)
dashboard_button.place(x=1,y=80)
addnew_cargo=Button(root, text="Add New Cargo", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                    fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc", command=add_new_cargo)
addnew_cargo.place(x=1,y=129)
View_cargo=Button(root, text="View Cargo Details", font=("Herald", 13,"bold"),height=2,  width=22, bg='#363740',
                  fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc", command=viewcargo)
View_cargo.place(x=1,y=178)
invoiceDetails=Button(root, text="Invoice Details", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740',
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc", command=view_invoice_details)
invoiceDetails.place(x=1,y=227)
employee_button=Button(root, text="Employee", font=("Herald", 13,"bold"), height=2, width=22, bg='#363740', 
                fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc",command=employee)
employee_button.place(x=1,y=276)


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
Logout.place(x=1,y=325)
# Button to display employees
display_button = tk.Button(root, text="Display Cargo", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, command=display_cargo)
display_button.place(x=1070, y=758)


root.mainloop()