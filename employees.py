
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pymysql

def connectDatabase():
   try:
      connection = pymysql.connect(host='localhost', user='root', password='rossi202')
      cursor = connection.cursor()
   except:
      messagebox.showerror('Error', 'Database Connectivity Issue, Plesase open mysql comand line client')
      return None, None
  
   return cursor,connection

def createDatabaseTable():
   cursor,connection=connectDatabase()
   cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
   cursor.execute('USE inventory_system')
   cursor.execute('CREATE TABLE IF NOT EXISTS employee_data (empid INT PRIMARY KEY, name VARCHAR(100), address VARCHAR(200), phone VARCHAR(500), idcard VARCHAR(50), salary VARCHAR(50))')

def treeviewData():
   cursor, connection=connectDatabase()
   if not cursor or not connection:
      return
   cursor.execute('use inventory_system')
   try:
      cursor.execute('SELECT * FROM employee_data')
      employeeRecord=cursor.fetchall()
      employeeTreview.delete(*employeeTreview.get_children())
      for record in employeeRecord:
         employeeTreview.insert('', END, values=record)
   except Exception as e:
      messagebox.showerror('Error', 'Error due to {e}')
   finally:
      cursor.close()
      connection.close()


def addEmployee(empid, name, address, idCard, phone, salary):
   if empid=='' or name=='' or address=='' or idCard=='' or phone=='' or salary=='':
      messagebox.showerror('Error', "Fill All Fields Required")
   else:
      cursor, connection=connectDatabase()
      if not cursor or not connection:
         return
      cursor.execute('use inventory_system')
      try:
         cursor.execute('INSERT INTO employee_data VALUES (%s,%s,%s,%s,%s,%s)', (empid, name, address, idCard, phone, salary))
         connection.commit()
         treeviewData()
         messagebox.showinfo('Success', 'Data is ineted Successfully')
      except Exception as e:
          messagebox.showerror('Error', 'Error due to {e}')
      finally:
         cursor.close()
         connection.close()

def selectData(event, empidEntry, nameEntry, addressEntry, idCardEntry, phoneEntry, salaryEntry):
   index=employeeTreview.selection()
   content=employeeTreview.item(index)
   row=content['values']
   clearFields(empidEntry, nameEntry, addressEntry, idCardEntry, phoneEntry, salaryEntry, False)
   empidEntry.insert(0, row[0])
   nameEntry.insert(1, row[1])
   addressEntry.insert(2, row[2])
   idCardEntry.insert(3, row[3])
   phoneEntry.insert(4, row[4])
   salaryEntry.insert(5, row[5])




def clearFields(empidEntry, nameEntry, addressEntry, idCardEntry, phoneEntry, salaryEntry, check):
   empidEntry.delete(0,END)
   nameEntry.delete(0,END)
   addressEntry.delete(0,END)
   idCardEntry.delete(0,END)
   phoneEntry.delete(0,END)
   salaryEntry.delete(0,END)
   if check:
      employeeTreview.selection_remove(employeeTreview.selection())

def updateEmployee(empid, name, address, idCard, phone, salary):
   selected=employeeTreview.selection()
   if not selected:
      messagebox.showerror('Error', 'No row is selected')
   else:
      cursor,connection=connectDatabase()
      if not cursor or not connection:
         return
      try:
         cursor.execute('use inventory_system')
         cursor.execute('SELECT * from employee_data WHERE empid=%s', (empid,))
         cursor.execute('UPDATE employee_data SET name=%s, address=%s, idcard=%s, phone=%s, salary=%s WHERE empid=%s', ( name, address, idCard, phone, salary, empid))
         connection.commit()
         treeviewData()
         messagebox.showinfo('Success', 'Data is Updated Successfully')
      except Exception as e:
         messagebox.showerror('Error', 'Error due to {e}')
      finally:
         cursor.close()
         connection.close()


def deleteEmployee(empid):
   selected=employeeTreview.selection()
   if not selected:
      messagebox.showerror('Error', 'No row is selected')
   else:
      result= messagebox.askyesno('Conform', 'Do you realy want to delete record')
      if result:
         cursor,connection=connectDatabase()
         if not cursor or not connection:
            return
         try:
            cursor.execute('use inventory_system')
            cursor.execute('DELETE FROM employee_data where empid=%s', (empid),)
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Record is Deleted Sucessfully')
         except Exception as e:
            messagebox.showerror('Error', 'Error due to {e}')
         finally:
            cursor.close()
            connection.close()

def searchEmployee(search_option, value):
   if search_option=='Search By':
      messagebox.showerror('Error', 'No option is Selected')
   elif value=='':
      messagebox.showerror('Error', 'Enter the value to search')
   else:
      cursor,connection=connectDatabase()
      if not cursor or not connection:
            return
      try:
         cursor.execute('use inventory_system')
         cursor.execute(f'SELECT * from employee_data WHERE {search_option} LIKE %s', f'%{value}%')
         records=cursor.fetchall()
         employeeTreview.delete(*employeeTreview.get_children())
         for record in records:
            employeeTreview.insert('',END,value=record)
      except Exception as e:
         messagebox.showerror('Error', 'Error due to {e}')
      finally:
         cursor.close()
         connection.close()




def employeeForm(root):
   global employeeTreview
   employeeFrame=Frame(root, width=1070, height=567)
   employeeFrame.place(x=200, y=105)
   headingLabel= Label(employeeFrame,text="Manage Employee Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
   headingLabel.place(x=0, y=0,  relwidth=1)

   backButton = Button(employeeFrame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E')
   backButton.place(x=10, y=30)

   topFrame = Frame(employeeFrame)
   topFrame.place(x=0, y=80, relwidth=1, height=235)
   searchFrame = Frame(topFrame)
   searchFrame.pack()
   searchCombo = ttk.Combobox(searchFrame, values=('id', 'Name', 'Phone#'), font=('times new roman', 12), state="readonly")
   searchCombo.set("Search By")
   searchCombo.grid(row=0, column=0, padx=20)
   searchEntery= Entry(searchFrame, font=('times new roman', 12), bg='lightyellow')
   searchEntery.grid(row=0, column=1, padx=20)
   searchButton= Button(searchFrame,  text="Search", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 10, 'bold'), cursor="hand2", command= lambda :searchEmployee(searchCombo.get(), searchEntery.get()))
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

   treeviewData()
   


   detailFrame= Frame(employeeFrame)
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

   addButtonFrame = Frame(employeeFrame)
   addButtonFrame.place(x=250, y=400)

   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Add", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :addEmployee(empidEntry.get(), nameEntry.get(), addressEntry.get(), idCardEntry.get(), phoneEntry.get(), salaryEntry.get()))
   addButton.grid(row=0, column=0, padx=20)

   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Update",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command= lambda :updateEmployee(empidEntry.get(), nameEntry.get(), addressEntry.get(), idCardEntry.get(), phoneEntry.get(), salaryEntry.get()))
   addButton.grid(row=0, column=1, padx=20)
  
   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Delete",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command= lambda :deleteEmployee(empidEntry.get(),))
   addButton.grid(row=0, column=2, padx=20)
  
   addButton = Button(addButtonFrame, padx=15, pady=5,  text="Clear",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :clearFields(empidEntry, nameEntry, addressEntry, idCardEntry, phoneEntry, salaryEntry, True))
   addButton.grid(row=0, column=3, padx=20)

   employeeTreview.bind('<ButtonRelease-1>',lambda event:selectData(event, empidEntry, nameEntry, addressEntry, idCardEntry, phoneEntry, salaryEntry))
   createDatabaseTable()