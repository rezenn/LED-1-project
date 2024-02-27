from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk

def invoicedetails():
    root.destroy()
    import invoiceDetails

def employee():
    root.destroy()
    import employees



def viewcargo():
    root.destroy()
    import View_cargodetails
#test function
def add_new_cargo():
    root.destroy()
    import addnewcargo

def dashboard():
    root.destroy()
    import dashboard






def display_employees():
    print("Displaying employees...")
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    # Clear existing data in the table
    for row in tree.get_children():
        tree.delete(row)

    # Insert the fetched rows into the table
    for row in rows:
        tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    conn.close()



# Add New Employee Function
def add_employee():
    print("Adding employee...")
    # Fetch employee details from entry fields
    employee_id = employee_id_entry.get()
    name = name_entry.get()
    post = post_entry.get()
    address = Address_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    username = username_entry.get()
    

    print("Employee ID:", employee_id)
    print("Name:", name)  
    print("Post:", post)
    print("Address:", address)
    print("Email:", email)
    print("Contact:", contact)
    print("Username:", username)


# Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()

    # Execute the SQL query to insert employee data
    cursor.execute("INSERT INTO employees (employee_id, name, post, address, email, contact, username ) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (employee_id, name, post, address, email, contact, username))
    conn.commit()
    messagebox.showinfo("Status", "Employee added successfully")

    conn.close()

    clear_entries()

def clear_entries():
    employee_id_entry.delete(0,'end')
    post_entry.delete(0,'end')
    Address_entry.delete(0,'end')
    name_entry.delete(0, 'end')
    contact_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    username_entry.delete(0,'end')

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an employee to delete.")
        return
    
    for item in selected_item:
        # Get the employee ID from the selected item
        employee_id = tree.item(item, 'values')[0]

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()

    # Execute the SQL query to delete the selected employee
    cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
    conn.commit()
    messagebox.showinfo("Status", "Employee deleted successfully")

    conn.close()
    tree.delete(selected_item)

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Please select an employee to update.")
        return

    # Get the employee ID from the selected item
    employee_id = tree.item(selected_item, 'values')[0]

    updated_name = name_entry.get()
    updated_post = post_entry.get()
    updated_address = Address_entry.get()
    updated_email = email_entry.get()
    updated_contact = contact_entry.get()
    updated_username = username_entry.get()

    print("Employee ID:", employee_id)
    print("Updated Name:", updated_name)
    print("Updated Post:", updated_post)
    print("Updated Address:", updated_address)
    print("Updated Email:", updated_email)
    print("Updated Contact:", updated_contact)
    print("Updated Username:", updated_username)

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cargo_mngt"
    )
    cursor = conn.cursor()

    cursor.execute("UPDATE employees SET username = %s, name = %s, post = %s, address = %s, email = %s, contact = %s WHERE employee_id = %s",
                   ( updated_username, updated_name, updated_post, updated_address, updated_email, updated_contact,employee_id))
    conn.commit()
    messagebox.showinfo("Status", "Employee information updated successfully")

    conn.close()

    display_employees()
root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Add New Cargo')
root.iconbitmap("cargo_icon.ico")

Frame1=Frame(root, height="677",width="977", bg="#e0dcdc")
Frame1.place(x=260, y=80)

#heading
Label1=Label(root, text="Employees", font=("Rubik one", 20), bg="#faeded")
Label1.place(x=265, y=30)


tableframe=Frame(root, bd=15,relief=RIDGE, bg="#e0dcdc")
tableframe.place(x=265,y=90,width=965,height=660)

#writing   ePART

name_label=Label(root, text="Employee Name:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
name_label.place(x=300, y=108)

name_entry=Entry(root, width=30, font=("Herald", 11))
name_entry.place(x=460, y=108)

post_label=Label(root, text="Employee post:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
post_label.place(x=300, y=138)

post_entry=Entry(root, width=30, font=("Herald", 11))
post_entry.place(x=460, y=138)

Address_label=Label(root, text="Address:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
Address_label.place(x=300, y=168)

Address_entry=Entry(root, width=30, font=("Herald", 11))
Address_entry.place(x=460, y=168)

email_label=Label(root, text="Email:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
email_label.place(x=300, y=198)

email_entry=Entry(root, width=30, font=("Herald", 11))
email_entry.place(x=460, y=198)

contact_label=Label(root, text="Contact:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
contact_label.place(x=300, y=228)

contact_entry=Entry(root, width=30, font=("Herald", 11))
contact_entry.place(x=460, y=228)

username_label=Label(root, text="Username:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
username_label.place(x=300, y=258)

username_entry=Entry(root,width=30, font=("Herald", 11))
username_entry.place(x=460, y=258)

employee_id_label=Label(root, text="Employee ID:", font=("Mulish", 12, 'bold' ), bg=('#e0dcdc'))
employee_id_label.place(x=300, y=288)

employee_id_entry=Entry(root,width=30, font=("Herald", 11))
employee_id_entry.place(x=460, y=288)


# Button
add=Button(root, text="Add", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1, command=add_employee)
add.place(x=350, y=675)

update=Button(root, text="Update", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1, command=update_employee)
update.place(x=650, y=675)

delete=Button(root, text="Delete", font=("Mulish", 18), bg = ("#8E8EBC"),fg="White", width=10 , height=1, command=delete_employee)
delete.place(x=960, y=675)

#frame

Frame2=Frame(root, height="800",width="231", bg="#363740")
Frame2.place(x=0, y=1)


#left side




cargo=Label(root, text="Cargo Management System", font=('Herald', 11, 'bold'), bg=('#363740'), fg='white')
cargo.place(x=28,y=2)


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
                 fg='white', bd=0, cursor="hand2", activebackground="#e0dcdc", command=invoicedetails)
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


#TABLE

# Create a Frame for the table
frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
frame.place(x=293, y=324, width=908, height=335)

# Create a Treeview widget (table)
tree = ttk.Treeview(frame, columns=("ID", "Name", "Post", "Address", "Email", "Contact", "Username"), show="headings")
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Post', text='Post')
tree.heading('Address', text='Address')
tree.heading('Email', text='Email')
tree.heading('Contact', text='Contact')
tree.heading('Username', text='Username')

# Add cells to the table
tree.column("ID", width=80, anchor=tk.CENTER)
tree.column("Name", width=150, anchor=tk.CENTER)
tree.column("Post", width=100, anchor=tk.CENTER)
tree.column("Address", width=200, anchor=tk.CENTER)
tree.column("Email", width=150, anchor=tk.CENTER)
tree.column("Contact", width=100, anchor=tk.CENTER)
tree.column("Username", width=100, anchor=tk.CENTER)


# Place the table on the window
tree.pack(fill=tk.BOTH, expand=True)

# Button to display employees
display_button = tk.Button(root, text="Display Employees", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, command=display_employees)
display_button.place(x=1070, y=760)

root.mainloop()
