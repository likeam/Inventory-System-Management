from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connectDatabase





def addSupplier(invoice, name,  contact, description):
    if invoice=='' or name==''  or contact=='' or description=='':
      messagebox.showerror('Error', "Fill All Fields Required")
    else:
        cursor, connection=connectDatabase()
        if not cursor or not connection:
            return
        cursor.execute('use inventory_system')
        cursor.execute('CREATE TABLE IF NOT EXISTS supplier_data (invoice INT PRIMARY KEY, name VARCHAR(100), contact VARCHAR(50), description TEXT)')
        cursor.execute('SELECT * from supplier_data WHERE invoice=%s', invoice)
        if cursor.fetchone():
           messagebox.showerror('Error', 'Inovice no is already exists' )
           return
       
        try:
            cursor.execute('INSERT INTO supplier_data VALUES (%s,%s,%s,%s)', (invoice, name,  contact, description))
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Data is ineted Successfully')
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()

def updateSupplier(invoice, name, contact, description):
    selected=treeview.selection()
    if not selected:
      messagebox.showerror('Error', 'No row is selected')
      return    
    cursor,connection=connectDatabase()
    if not cursor or not connection:
        return
    try:
      cursor.execute('use inventory_system')
      cursor.execute('SELECT * from supplier_data WHERE invoice=%s', (invoice,))
      cursor.execute('UPDATE supplier_data SET name=%s,  contact=%s, description=%s WHERE invoice=%s', ( name, contact, description, invoice))
      connection.commit()
      treeviewData()
      messagebox.showinfo('Success', 'Data is Updated Successfully')
    except Exception as e:
        messagebox.showerror('Error', 'Error due to {e}')
    finally:
        cursor.close()
        connection.close()

def deleteSupplier(invoice):
   selected=treeview.selection()
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
            cursor.execute('DELETE FROM supplier_data where invoice=%s', (invoice),)
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Record is Deleted Sucessfully')
         except Exception as e:
            messagebox.showerror('Error', 'Error due to {e}')
         finally:
            cursor.close()
            connection.close()

def clearFields(invoiceEntry, nameEntry, contactEntry, descriptionText, check):
   invoiceEntry.delete(0,END)
   nameEntry.delete(0,END)
   contactEntry.delete(0,END)
   descriptionText.delete(1.0,END)
   if check:
      treeview.selection_remove(treeview.selection())


def selectData(event,invoiceEntry, nameEntry,  contactEntry, descriptionText):
   index=treeview.selection()
   content=treeview.item(index)
   row=content['values']
   clearFields(invoiceEntry, nameEntry,  contactEntry, descriptionText, False)
   invoiceEntry.insert(0, row[0])
   nameEntry.insert(0, row[1])
   contactEntry.insert(0, row[2])
   descriptionText.insert(1.0, row[3])
 


def treeviewData():
   cursor, connection=connectDatabase()
   if not cursor or not connection:
      return
   cursor.execute('use inventory_system')
   try:
      cursor.execute('SELECT * FROM supplier_data')
      supplierRecord=cursor.fetchall()
      treeview.delete(*treeview.get_children())
      for record in supplierRecord:
         treeview.insert('', END, values=record)
   except Exception as e:
      messagebox.showerror('Error', 'Error due to {e}')
   finally:
      cursor.close()
      connection.close()

def searchSupplier(invoice):   
   if invoice=='':
      messagebox.showerror('Error', 'Enter the value to search')
   else:
      cursor,connection=connectDatabase()
      if not cursor or not connection:
            return
      try:
        cursor.execute('use inventory_system')
        cursor.execute('SELECT * from supplier_data WHERE invoice=%s', invoice)
        record=cursor.fetchone()
        treeview.delete(*treeview.get_children())        
        treeview.insert('',END,values=record)
      except Exception as e:
        messagebox.showerror('Error', 'Error due to {e}')
      finally:
        cursor.close()
        connection.close()

def showAll(searchEntery):
   treeviewData()
   searchEntery.delete(0,END)
 


def supplierForm(root):
    global treeview
    supplierFrame=Frame(root, width=1070, height=567)
    supplierFrame.place(x=200, y=105)

    headingLabel= Label(supplierFrame,text="Manage Supplier Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
    headingLabel.place(x=0, y=0,  relwidth=1)

    backButton = Button(supplierFrame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E', command=lambda : supplierFrame.place_forget())
    backButton.place(x=10, y=30)


    leftFrame = Frame(supplierFrame)
    leftFrame.place(x=10, y=100, relwidth=1, height=300)
    
    invoiceLabel= Label(leftFrame, text='Invoice No.', font=('times new roman', 14, 'bold'))
    invoiceLabel.grid(row=0, column=0, padx=(20, 40), pady=10, sticky='w')
    invoiceEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    invoiceEntry.grid(row=0, column=1, padx=20, pady=10)

    nameLabel= Label(leftFrame, text='Supplier Name', font=('times new roman', 14, 'bold'))
    nameLabel.grid(row=1, column=0, padx=(20, 40), pady=10, sticky='w')
    nameEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    nameEntry.grid(row=1, column=1, padx=20, pady=10)

    contactLabel= Label(leftFrame, text='Contact', font=('times new roman', 14, 'bold'))
    contactLabel.grid(row=3, column=0, padx=(20, 40), pady=10, sticky='w')
    contactEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'), bg='lightyellow')
    contactEntry.grid(row=3, column=1, padx=20, pady=10)

    descriptionLabel= Label(leftFrame, text='Description', font=('times new roman', 14, 'bold'))
    descriptionLabel.grid(row=4, column=0, padx=(20, 40), sticky='nw')
    descriptionText = Text(leftFrame, font=('times new roman', 14, 'bold'), bg='lightyellow', width=20, height=6, bd=2)
    descriptionText.grid(row=4, column=1,padx=20, pady=10)

    buttonFrame = Frame(supplierFrame)
    buttonFrame.place(x=70, y=410)

    addButton = Button( buttonFrame, padx=5, pady=5,  text="Add", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :addSupplier(invoiceEntry.get(), nameEntry.get(),  contactEntry.get(), descriptionText.get(1.0,END).strip()))
    addButton.grid(row=0, column=0, padx=5)

    updateButton = Button( buttonFrame, padx=5, pady=5,  text="Update",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :updateSupplier(invoiceEntry.get(), nameEntry.get(), contactEntry.get(), descriptionText.get(1.0,END).strip()))
    updateButton.grid(row=0, column=1, padx=5)
    
    deleteButton = Button( buttonFrame, padx=5, pady=5,  text="Delete",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :deleteSupplier(invoiceEntry.get(),))
    deleteButton.grid(row=0, column=2, padx=5)
    
    clearButton = Button( buttonFrame, padx=5, pady=5,  text="Clear",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2",  command=lambda :clearFields(invoiceEntry, nameEntry, contactEntry, descriptionText,  True))
    clearButton.grid(row=0, column=3, padx=5)

    rightFrame = Frame(supplierFrame)
    rightFrame.place(x=450, y=115)

    searchFrame = Frame(rightFrame)
    searchFrame.pack()

    searchLabel= Label(searchFrame, text='Invoice No.', font=('times new roman', 14, 'bold'))
    searchLabel.grid(row=0, column=0, padx=(20, 40), pady=10, sticky='w')
    searchEntry = Entry(searchFrame, font=('times new roman', 14, 'bold'), bg='lightyellow', width=10)
    searchEntry.grid(row=0, column=1, padx=20, pady=10)

    searchButton = Button(searchFrame, padx=5, pady=2,  text="Search",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command= lambda :searchSupplier(searchEntry.get(),))
    searchButton.grid(row=0, column=2, padx=5)
    
    showButton = Button(searchFrame, padx=5, pady=2,  text="Show All",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command= lambda :showAll(searchEntry.get(),))
    showButton.grid(row=0, column=3, padx=5)

    horizentalScrollbar = Scrollbar(rightFrame, orient=HORIZONTAL)
    verticalScrollbar = Scrollbar(rightFrame, orient=VERTICAL)
    treeview = ttk.Treeview(rightFrame, columns=('invoice','name','contact','description'), show='headings', yscrollcommand=verticalScrollbar.set, xscrollcommand=horizentalScrollbar.set)
    horizentalScrollbar.pack(side=BOTTOM, fill=X )
    verticalScrollbar.pack(side=RIGHT, fill=Y)
    horizentalScrollbar.config(command=treeview.xview)
    verticalScrollbar.config(command=treeview.yview)
    treeview.pack(pady=(10, 0))

    treeview.heading('invoice', text="Invoice")
    treeview.heading('name', text="Name")
    treeview.heading('contact', text="Contact")
    treeview.heading('description', text="Description")

    treeview.column('invoice', width=60)
    treeview.column('name', width=120)
    treeview.column('contact', width=120)
    treeview.column('description', width=160)

    treeviewData()
    treeview.bind('<ButtonRelease-1>',lambda event:selectData(event, invoiceEntry, nameEntry,  contactEntry, descriptionText))


    