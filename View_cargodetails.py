from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry('1280x800')
root.resizable(0, 0)
root.title('Cargo Status')



#heading

Label1=Label(root, text="View Cargo Details ", font=("Rubik one", 20))
Label1.place(x=265, y=30)


#frame

Frame1=Frame(root, height="670",width="930", bg="#e0dcdc")
Frame1.place(x=260, y=80)

tableframe=Frame(root, bd=15,relief=RIDGE)
tableframe.place(x=265,y=90,width=920,height=650)


scroll_x=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y=ttk.Scrollbar(tableframe,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

cargo_detail_table=ttk.Treeview(tableframe,column=("Con ID", "Sender","S-Contact","S-Country","S-ZIP Code", "Receiver","R-Contact", "R-Country","R-ZIP Code")
                                ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


scroll_x.config(side=BOTTOM,fill=X)
scroll_y.config(side=RIGHT,fill=Y)







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