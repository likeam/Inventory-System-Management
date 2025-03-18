from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connectDatabase


def addCategory(id, name, description):
    if id=='' or name=='' or description=='':
      messagebox.showerror('Error', "Fill All Fields Required")
    else:
        cursor, connection=connectDatabase()
        if not cursor or not connection:
            return
        cursor.execute('use inventory_system')
        cursor.execute('CREATE TABLE IF NOT EXISTS category_data (id INT PRIMARY KEY, name VARCHAR(100), description TEXT)')
        cursor.execute('SELECT * from category_data WHERE id=%s', id)
        if cursor.fetchone():
           messagebox.showerror('Error', 'ID no is already exists' )
           return
        try:
            cursor.execute('INSERT INTO category_data VALUES (%s,%s,%s)', (id, name, description))
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Data is ineted Successfully')
            clearFields(id, name, description)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {e}')
        finally:
            cursor.close()
            connection.close()

def deleteCategory(id):
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
            cursor.execute('DELETE FROM category_data where id=%s', (id),)
            connection.commit()
            treeviewData()
            messagebox.showinfo('Success', 'Record is Deleted Sucessfully')            
         except Exception as e:
            messagebox.showerror('Error', 'Error due to {e}')
         finally:
            cursor.close()
            connection.close()


def clearFields(idEntry, nameEntry, descriptionText):
   idEntry.delete(0,END)
   nameEntry.delete(0,END)
   descriptionText.delete(1.0,END)


def treeviewData():
   cursor, connection=connectDatabase()
   if not cursor or not connection:
      return
   cursor.execute('use inventory_system')
   try:
      cursor.execute('SELECT * FROM category_data')
      supplierRecord=cursor.fetchall()
      treeview.delete(*treeview.get_children())
      for record in supplierRecord:
         treeview.insert('', END, values=record)
   except Exception as e:
      messagebox.showerror('Error', 'Error due to {e}')
   finally:
      cursor.close()
      connection.close()


def clearFields(idEntry, nameEntry, descriptionText):
   idEntry.delete(0,END)
   nameEntry.delete(0,END)
   descriptionText.delete(1.0,END)


def selectData(event,idEntry, nameEntry, descriptionText):
   index=treeview.selection()
   content=treeview.item(index)
   row=content['values']
   clearFields(idEntry, nameEntry, descriptionText)
   idEntry.insert(0, row[0])
   nameEntry.insert(0, row[1])
   descriptionText.insert(1.0, row[2])
   

def categoryForm(root):
    global logo, treeview
    categoryFrame=Frame(root, width=1070, height=567)
    categoryFrame.place(x=200, y=105)

    headingLabel= Label(categoryFrame,text="Manage Categories Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
    headingLabel.place(x=0, y=0,  relwidth=1)

    backButton = Button(categoryFrame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E', command=lambda : categoryFrame.place_forget())
    backButton.place(x=10, y=30)

    logo=PhotoImage(file='product.png')
    label=Label(categoryFrame, image=logo)
    label.place(x=30, y=100)

    detailFrame=Frame(categoryFrame)
    detailFrame.place(x=400, y=30)
    
    idLabel= Label(detailFrame, text='ID', font=('times new roman', 14, 'bold'))
    idLabel.grid(row=0, column=0, padx=(20, 40), pady=10, sticky='w')
    idEntry = Entry(detailFrame, font=('times new roman', 14, 'bold'), bg='white')
    idEntry.grid(row=0, column=1, padx=20, pady=10)

    nameLabel= Label(detailFrame, text='Category Name', font=('times new roman', 14, 'bold'))
    nameLabel.grid(row=1, column=0, padx=(20, 40), pady=10, sticky='w')
    nameEntry = Entry(detailFrame, font=('times new roman', 14, 'bold'), bg='white')
    nameEntry.grid(row=1, column=1, padx=20, pady=10)

    descriptionLabel= Label(detailFrame, text='Description', font=('times new roman', 14, 'bold'))
    descriptionLabel.grid(row=2, column=0, padx=(20, 40), sticky='nw')
    descriptionText = Text(detailFrame, font=('times new roman', 14, 'bold'), bg='white', width=20, height=4, bd=2)
    descriptionText.grid(row=2, column=1,padx=20, pady=10)


    buttonFrame = Frame(categoryFrame)
    buttonFrame.place(x=640, y=240)

    addButton = Button( buttonFrame, padx=5, pady=5,  text="Add", bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :addCategory(idEntry.get(), nameEntry.get(),  descriptionText.get(1.0,END).strip()))
    addButton.grid(row=0, column=0, padx=5)
   
    deleteButton = Button( buttonFrame, padx=5, pady=5,  text="Delete",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2", command=lambda :deleteCategory(idEntry.get()))
    deleteButton.grid(row=0, column=2, padx=5)

    clearButton = Button( buttonFrame, padx=5, pady=5,  text="Clear",  bg='#9E9E9E', fg='#E0E0E0', font=('times new roman', 15, 'bold'), cursor="hand2",  command=lambda :clearFields(idEntry, nameEntry, descriptionText))
    clearButton.grid(row=0, column=3, padx=5)

    treeviewFrame=Frame(categoryFrame)
    treeviewFrame.place(x=430, y=295, width=620)

    horizentalScrollbar = Scrollbar(treeviewFrame, orient=HORIZONTAL)
    verticalScrollbar = Scrollbar(treeviewFrame, orient=VERTICAL)
    treeview = ttk.Treeview(treeviewFrame, columns=('id','name','description'), show='headings', yscrollcommand=verticalScrollbar.set, xscrollcommand=horizentalScrollbar.set)
    horizentalScrollbar.pack(side=BOTTOM, fill=X )
    verticalScrollbar.pack(side=RIGHT, fill=Y)
    horizentalScrollbar.config(command=treeview.xview)
    verticalScrollbar.config(command=treeview.yview)
    treeview.pack(pady=(10, 0))

    treeview.heading('id', text="ID")
    treeview.heading('name', text="Category Name")
    treeview.heading('description', text="Description")

    treeview.column('id', width=120)
    treeview.column('name', width=180)
    treeview.column('description', width=360)

    treeviewData()
    treeview.bind('<ButtonRelease-1>',lambda event:selectData(event, idEntry, nameEntry, descriptionText))