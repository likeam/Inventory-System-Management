
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql




   



def employee_form(root):
   employee_frame=Frame(root, width=1070, height=567)
   employee_frame.place(x=200, y=105)
   headingLabel= Label(employee_frame,text="Manage Employee Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
   headingLabel.place(x=0, y=0,  relwidth=1)

   backButton = Button(employee_frame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E')
   backButton.place(x=10, y=30)

   topFrame = Frame(employee_frame)
   topFrame.place(x=0, y=80, relwidth=1, height=235)
   searchFrame = Frame(topFrame)
   searchFrame.pack()
   searchCombo = ttk.Combobox(searchFrame, values=('id', 'Name', 'Eamil'), font=('times new roman', 12), state="readonly")
   searchCombo.set("Search By")
   searchCombo.grid(row=0, column=0, padx=20)
   searchEntery= Entry(searchFrame, font=('times new roman', 12), bg='lightyellow')
   searchEntery.grid(row=0, column=1, padx=20)
   searchButton= Button(searchFrame,  text="Search", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 10, 'bold'), cursor="hand2")
   searchButton.grid(row=0,column=2, padx=20)
   searchButton= Button(searchFrame,  text="Show All", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 10, 'bold'), cursor="hand2")
   searchButton.grid(row=0,column=3, padx=20)

   horizentalScrollbar = Scrollbar(topFrame, orient=HORIZONTAL)
   verticalScrollbar = Scrollbar(topFrame, orient=VERTICAL)
   employeeTreview = ttk.Treeview(topFrame, columns=('empid', 'name', 'address', 'idcard', 'phone', 'salary'), show='headings', yscrollcommand=verticalScrollbar.set, xscrollcommand=horizentalScrollbar.set)
   horizentalScrollbar.pack(side=BOTTOM, fill=X )
   verticalScrollbar.pack(side=RIGHT, fill=Y)
   horizentalScrollbar.config(command=employeeTreview.xview)
   verticalScrollbar.config(command=employeeTreview.yview)
   employeeTreview.pack(pady=(10, 0))

   employeeTreview.heading('empid', text="EmpId")
   employeeTreview.heading('name', text="Name")
   employeeTreview.heading('address', text="Adress")
   employeeTreview.heading('idcard', text="ID-Card#")
   employeeTreview.heading('phone', text="Phone#")
   employeeTreview.heading('salary', text="Salary")

   employeeTreview.column('empid', width=60)
   employeeTreview.column('name', width=140)
   employeeTreview.column('address', width=200)
   employeeTreview.column('idcard', width=140)
   employeeTreview.column('phone', width=140)
   employeeTreview.column('salary', width=140)


   detailFrame= Frame(employee_frame)
   detailFrame.place(x=0, y=300)

   empIdLabel= Label(detailFrame, text='EmpId', font=('times new roman', 12))
   empIdLabel.grid(row=0, column=0, padx=20, pady=10)
   empidEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   empidEntry.grid(row=0, column=1, padx=20, pady=10)

   nameLabel= Label(detailFrame, text='Name', font=('times new roman', 12))
   nameLabel.grid(row=0, column=2, padx=20, pady=10)
   nameEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   nameEntry.grid(row=0, column=3, padx=20, pady=10)

   addressLabel= Label(detailFrame, text='Address', font=('times new roman', 12))
   addressLabel.grid(row=0, column=4, padx=20, pady=10)
   addressEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   addressEntry.grid(row=0, column=5, padx=20, pady=10)
  
   idCardLabel= Label(detailFrame, text='ID Card #', font=('times new roman', 12))
   idCardLabel.grid(row=1, column=0, padx=20, pady=10)
   idCardEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   idCardEntry.grid(row=1, column=1, padx=20, pady=10)

   phoneLabel= Label(detailFrame, text='Phone', font=('times new roman', 12))
   phoneLabel.grid(row=1, column=2, padx=20, pady=10)
   phoneEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   phoneEntry.grid(row=1, column=3, padx=20, pady=10)

   salaryLabel= Label(detailFrame, text='Salary', font=('times new roman', 12))
   salaryLabel.grid(row=1, column=4, padx=20, pady=10)
   salaryEntry = Entry(detailFrame, font=('times new roman', 12), bg='lightyellow')
   salaryEntry.grid(row=1, column=5, padx=20, pady=10)

   addButtonFrame = Frame(employee_frame)
   addButtonFrame.place(x=250, y=400)

   # , command=addEmployee(empidEntry.get(), nameEntry.get(), addressEntry.get(), idCardEntry.get(),  phoneEntry.get(), salaryEntry.get())

   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Add", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2")
   addButton.grid(row=0, column=0, padx=20)

   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Update",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2")
   addButton.grid(row=0, column=1, padx=20)
  
   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Delete",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2")
   addButton.grid(row=0, column=2, padx=20)
  
   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Clear",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2")
   addButton.grid(row=0, column=3, padx=20)