from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connectDatabase


def treeviewData():
   cursor, connection=connectDatabase()
   if not cursor or not connection:
      return
   cursor.execute('use inventory_system')
   try:
      cursor.execute('SELECT * FROM product_data')
      productRecord=cursor.fetchall()
      treeview.delete(*treeview.get_children())
      for record in productRecord:
         treeview.insert('', END, values=record)
   except Exception as e:
      messagebox.showerror('Error', 'Error due to {e}')
   finally:
      cursor.close()
      connection.close()

def fetchSupplierCategory(categoryCombobox, supplierCombobox):
      categoryOption=[]
      supplierOption=[]
      cursor, connection=connectDatabase()
      if not cursor or not connection:
         return
      cursor.execute('use inventory_system')
      cursor.execute('SELECT name from category_data')
      names=cursor.fetchall()
      if len(names)>0:
          categoryCombobox.set('Select')
      for name in names:
        categoryOption.append(name[0])
      categoryCombobox.config(values=categoryOption)

      cursor.execute('SELECT name from supplier_data')
      names=cursor.fetchall()
      if len(names)>0:
          categoryCombobox.set('Select')
      for name in names:
        supplierOption.append(name[0])
      supplierCombobox.config(values=supplierOption)



def addProduct(category, supplier, name, price, quantity, status, categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, check):
   if category=='Empty':  
        messagebox.showerror('Error', "Please Select Category Field")
   elif supplier=='Empty':
        messagebox.showerror('Error', "Please Select Supplier Field")
   elif category=='Select' or supplier=='Select' or name=='' or price=='' or quantity=='' or status=='Select Status':
       messagebox.showerror('Error', "Please all Field are required")
   else:
      cursor, connection=connectDatabase()
      if not cursor or not connection:
         return
      cursor.execute('use inventory_system')
      cursor.execute('CREATE TABLE IF NOT EXISTS product_data (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(100), supplier VARCHAR(100), name VARCHAR(100), price INT, quantity INT, status VARCHAR(50))')
      cursor.execute('SELECT * from product_data WHERE category=%s AND supplier=%s AND name=%s', (category, supplier, name, ))
      existingProduct = cursor.fetchone()
      if existingProduct:
         messagebox.showerror('Error', "Product  allready Exists")
         return
      cursor.execute('INSERT INTO product_data (category,supplier,name,price,quantity,status) VALUES(%s,%s,%s,%s,%s,%s)', (category, supplier, name, price, quantity, status))
      connection.commit()
      messagebox.showinfo('Success', 'Data is ineted Successfully')
      clearFields(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox,treeview, check)
      treeviewData()

def updateProduct(category, supplier, name, price, quantity, status,categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, check):
    selected=treeview.selection()
    dist=treeview.item(selected)
    content=dist['values']
    id=content[0]
    if not selected:
      messagebox.showerror('Error', 'No row is selected')
      return    
    cursor,connection=connectDatabase()
    if not cursor or not connection:
        return
    try:
      cursor.execute('use inventory_system')
      cursor.execute('SELECT * from product_data WHERE id=%s', id)
      currentData=cursor.fetchone()
      currentData= currentData[1:]
      quantity=int(quantity)
      newData = (category, supplier, name, price, quantity, status)
      if currentData == newData:
         messagebox.showinfo('Info', 'No Changes detected')
         return      
      cursor.execute('UPDATE product_data SET category=%s,  supplier=%s, name=%s, price=%s, quantity=%s, status=%s WHERE id=%s', (category, supplier, name, price, quantity, status, id ))
      connection.commit()
      treeviewData()
      messagebox.showinfo('Success', 'Data is Updated Successfully')
      clearFields(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox,treeview, check)
    except Exception as e:
        messagebox.showerror('Error', 'Error due to {e}')
    finally:
        cursor.close()
        connection.close()


def deleteProduct(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox,treeview, check):
   selected=treeview.selection()
   dist=treeview.item(selected)
   content=dist['values']
   id=content[0]
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
            cursor.execute('DELETE FROM product_data where id=%s', id)
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Record is Deleted Sucessfully')
            clearFields(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox,treeview, check)
         except Exception as e:
            messagebox.showerror('Error', 'Error due to {e}')
         finally:
            cursor.close()
            connection.close()

def clearFields(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox,treeview, check):
   categoryCombobox.set('Select')
   supplierCombobox.set('Select')
   nameEntry.delete(0,END)
   priceEntry.delete(0,END)
   quantityEntry.delete(0,END)
   statusCombobox.set('Select')   
   if check:
      treeview.selection_remove(treeview.selection())


def selectData(event, categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox):
   index=treeview.selection()
   content=treeview.item(index)
   row=content['values']
   nameEntry.delete(0,END)
   priceEntry.delete(0,END)
   quantityEntry.delete(0,END)
   categoryCombobox.set(row[1])
   supplierCombobox.set(row[2])
   nameEntry.insert(0, row[3])
   priceEntry.insert(0, row[4])
   quantityEntry.insert(0, row[5])
   statusCombobox.set(row[6])


   
def searchProduct(search_option, value):
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
         cursor.execute(f'SELECT * from product_data WHERE {search_option} LIKE %s', f'%{value}%')
         records=cursor.fetchall()
         treeview.delete(*treeview.get_children())
         for record in records:
            treeview.insert('',END,value=record)
      except Exception as e:
         messagebox.showerror('Error', 'Error due to {e}')
      finally:
         cursor.close()
         connection.close()

def showAll(searchCombo, searchEntery):
   treeviewData()
   searchEntery.delete(0,END)
   searchCombo.set('Search By')


      


def productForm(root):
    global treeview
    productFrame=Frame(root, width=1070, height=567)
    productFrame.place(x=200, y=105)

    headingLabel= Label(productFrame,text="Manage Products Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
    headingLabel.place(x=0, y=0,  relwidth=1)

    backButton = Button(productFrame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E', command=lambda :  productFrame.place_forget())
    backButton.place(x=10, y=30)

    leftFrame= Frame(productFrame, bd=4, padx=20, relief=RIDGE)
    leftFrame.place(x=40, y=90)

    headingLabel= Label(leftFrame,text="Manage Products Details", font=('times new roman', 14, 'bold'),  bg='#212529', fg='#E0E0E0')
    headingLabel.grid(row=0, columnspan=2, sticky='we')

    categoryLabel= Label(leftFrame,text="Category", font=('times new roman', 14, 'bold'))
    categoryLabel.grid(row=1, column=0, padx=10, sticky='w')
    categoryCombobox=ttk.Combobox(leftFrame, font=('Times new roman', 14, 'bold'), width=18, cursor="hand2", state='readonly')
    categoryCombobox.grid(row=1, column=1, pady=10)
    categoryCombobox.set('Empty')

    supplierLabel= Label(leftFrame,text="Supplier", font=('times new roman', 14, 'bold'))
    supplierLabel.grid(row=2, column=0, padx=10, sticky='w')
    supplierCombobox=ttk.Combobox(leftFrame, font=('Times new roman', 14, 'bold'), width=18, cursor="hand2", state='readonly')
    supplierCombobox.grid(row=2, column=1, pady=10)
    supplierCombobox.set('Empty')

    nameLabel= Label(leftFrame, text='Name', font=('times new roman', 14, 'bold'))
    nameLabel.grid(row=3, column=0, padx=10,  sticky='w')
    nameEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'))
    nameEntry.grid(row=3, column=1,  pady=10)

    priceLabel= Label(leftFrame, text='Price', font=('times new roman', 14, 'bold'))
    priceLabel.grid(row=4, column=0, padx=10, sticky='w')
    priceEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'))
    priceEntry.grid(row=4, column=1,  pady=10)

    quantityLabel= Label(leftFrame, text='Quantity', font=('times new roman', 14, 'bold'))
    quantityLabel.grid(row=5, column=0, padx=10, sticky='w')
    quantityEntry = Entry(leftFrame, font=('times new roman', 14, 'bold'))
    quantityEntry.grid(row=5, column=1,  pady=10)

    statusLabel= Label(leftFrame,text="Status", font=('times new roman', 14, 'bold'))
    statusLabel.grid(row=6, column=0, padx=10, sticky='w')
    statusCombobox=ttk.Combobox(leftFrame, values=('Active', 'Inactive'), font=('Times new roman', 14, 'bold'), width=18, cursor="hand2", state='readonly')
    statusCombobox.grid(row=6, column=1, pady=10)
    statusCombobox.set('Empty')

    buttonFrame = Frame(leftFrame)
    buttonFrame.grid(row=7, columnspan=2, pady=(30, 10))

    addButton = Button( buttonFrame, text="Add", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2", 
                       command=lambda :addProduct(categoryCombobox.get(), supplierCombobox.get(), nameEntry.get(), priceEntry.get(), quantityEntry.get(), statusCombobox.get(),categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, True))
    addButton.grid(row=0, column=0, padx=5)

    updateButton = Button( buttonFrame, text="Update",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2",
                           command=lambda :updateProduct(categoryCombobox.get(), supplierCombobox.get(), nameEntry.get(), priceEntry.get(), quantityEntry.get(), statusCombobox.get(),categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, True) )
    updateButton.grid(row=0, column=1, padx=5)
    
    deleteButton = Button( buttonFrame, text="Delete",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2",
                         command=lambda :deleteProduct(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, True))
    deleteButton.grid(row=0, column=2, padx=5)
    
    clearButton = Button( buttonFrame, text="Clear",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2",
                          command=lambda :clearFields(categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox, treeview, TRUE,))
    clearButton.grid(row=0, column=3, padx=5)

    searchFrame= LabelFrame(productFrame, text='Search Product', font=('Times new roman', 14, 'bold'))
    searchFrame.place(x=430, y=80)
    searchCombobox=ttk.Combobox(searchFrame, values=('Category', 'Supplier', 'Name', 'Status'), state='readonly', width=16,  font=('times new roman', 14, 'bold'))
    searchCombobox.grid(row=0, column=0, padx=(40, 10 ))
    searchCombobox.set('Search By')
    searchEntry = Entry(searchFrame, font=('times new roman', 14, 'bold'), width=16)
    searchEntry.grid(row=0, column=1, padx=10)
    searchButton = Button( searchFrame, text="Search",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2", command= lambda :searchProduct(searchCombobox.get(), searchEntry.get()))
    searchButton.grid(row=0, column=2, padx=5, pady=10)
    
    showAllButton = Button( searchFrame, text="Show All",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 14, 'bold'), cursor="hand2", command= lambda :showAll(searchCombobox, searchEntry))
    showAllButton.grid(row=0, column=3, padx=(5,40))

    treeviewFrame= LabelFrame(productFrame, text='Products', font=('Times new roman', 14, 'bold'))
    treeviewFrame.place(x=430, y=180, width=620, height=350)

    horizentalScrollbar = Scrollbar(treeviewFrame, orient=HORIZONTAL)
    verticalScrollbar = Scrollbar(treeviewFrame, orient=VERTICAL)
    treeview = ttk.Treeview(treeviewFrame, columns=('id', 'category', 'supplier', 'name', 'price', 'quantity', 'status' ), show='headings', yscrollcommand=verticalScrollbar.set, xscrollcommand=horizentalScrollbar.set)
    horizentalScrollbar.pack(side=BOTTOM, fill=X )
    verticalScrollbar.pack(side=RIGHT, fill=Y)
    horizentalScrollbar.config(command=treeview.xview)
    verticalScrollbar.config(command=treeview.yview)
    treeview.pack(pady=(10, 0))

    treeview.heading('id', text="ID")
    treeview.heading('category', text="Category")
    treeview.heading('supplier', text="Supplier")
    treeview.heading('name', text="Name")
    treeview.heading('price', text="Price")
    treeview.heading('quantity', text="Quantity")
    treeview.heading('status', text="Status")

    treeview.column('id', width=60)
    treeview.column('category', width=120)
    treeview.column('supplier', width=80)
    treeview.column('name', width=120)
    treeview.column('price', width=60)
    treeview.column('quantity', width=60)
    treeview.column('status', width=120)

    treeviewData()
    treeview.bind('<ButtonRelease-1>',lambda event:selectData(event, categoryCombobox, supplierCombobox, nameEntry, priceEntry, quantityEntry, statusCombobox))

    fetchSupplierCategory(categoryCombobox, supplierCombobox)



