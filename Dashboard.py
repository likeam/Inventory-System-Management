from tkinter import *
from tkinter import ttk

# Funcions

def employee_form():
   employee_frame=Frame(root, width=1070, height=567, bg='#87CEEB')
   employee_frame.place(x=200, y=105)
   headingLabel= Label(employee_frame,text="Manage Employee Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
   headingLabel.place(x=0, y=0,  relwidth=1)

   backButton = Button(employee_frame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2")
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
   searchButton= Button(searchFrame,  text="Search",  bg='#212529', fg='#E0E0E0', font=('times new roman', 10, 'bold'), cursor="hand2")
   searchButton.grid(row=0,column=2, padx=20)
   searchButton= Button(searchFrame,  text="Show All",bg='#212529', fg='#E0E0E0', font=('times new roman', 10, 'bold'), cursor="hand2")
   searchButton.grid(row=0,column=3, padx=20)
   


# GUI

root = Tk()

root.title("Dashboard")
root.geometry('1270x668+0+0')
root.resizable(0,0)
root.config(bg='gray')
bg_Image = PhotoImage(file='inventory.png')

titleLabel=Label(root, image=bg_Image, compound=LEFT, text='  Inventory Management System', font=('times new roman', 40 , 'bold'), bg='#212529', fg='#E0E0E0', anchor='w', padx=25, pady=10  )
titleLabel.place(x=0, y=0, relwidth=1)
logoutButton=Button(root, text='Logout', font=('times new roman', 20, 'bold'))
logoutButton.place(x=1100, y=10)
subtitleLabel = Label(root, text='Welcome Admin\t\t Date: 10-03-2025\t\t Time: 12:36:17 pm', font=('times new roman',15))
subtitleLabel.place(x=0, y=80, relwidth=1)
leftFrame = Frame(root)
leftFrame.place(x=0, y=110, width=200, height=555)
logo_Image = PhotoImage(file='logo.png')
imageLabel=Label(leftFrame, image=logo_Image)
imageLabel.pack()
menuLabel=Label(leftFrame, text="Menu", font=('times new roman', 20), bg='#212529', fg='#E0E0E0' )
menuLabel.pack(fill=X)
employe_Image = PhotoImage(file='employee.png')
employe_button=Button(leftFrame, image=employe_Image, compound=LEFT, text=' Employees', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',command=employee_form ,cursor="hand2")
employe_button.pack(fill=X)
supplier_Image = PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame, image=supplier_Image, compound=LEFT, text=' Supplier', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',cursor="hand2")
supplier_button.pack(fill=X)
category_Image = PhotoImage(file='category.png')
category_button=Button(leftFrame, image=category_Image, compound=LEFT, text=' Category', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',cursor="hand2")
category_button.pack(fill=X)
products_Image = PhotoImage(file='products.png')
products_button=Button(leftFrame, image=products_Image, compound=LEFT, text=' Products', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',cursor="hand2")
products_button.pack(fill=X)
sales_Image = PhotoImage(file='sale.png')
sales_button=Button(leftFrame, image=sales_Image, compound=LEFT, text=' Sales', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',cursor="hand2")
sales_button.pack(fill=X)
exit_Image = PhotoImage(file='exit.png')
exit_button=Button(leftFrame, image=exit_Image, compound=LEFT, text=' Exit', font=('times new roman', 20, 'bold'), bg='#E0E0E0', padx=10, anchor='w',cursor="hand2")
exit_button.pack(fill=X)

emp_frame=Frame(root, bg='#87CEEB', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=130, height=170, width=280)
total_emp_icon=PhotoImage(file='totalemployee.png')
total_emp_label=Label(emp_frame, image=total_emp_icon, bg='#87CEEB')
total_emp_label.pack()
total_emp_label_text=Label(emp_frame, text='Total Employees', bg='#87CEEB', fg='white', font=('times new roman', 15, 'bold'))
total_emp_label_text.pack()
total_emp_label_count=Label(emp_frame, text='0', bg='#87CEEB', fg='white', font=('times new roman', 30, 'bold'))
total_emp_label_count.pack()

supply_frame=Frame(root, bg='#5C62D6', bd=3, relief=RIDGE)
supply_frame.place(x=800, y=130, height=170, width=280)
total_supply_icon=PhotoImage(file='totalsupplier.png')
total_supply_label=Label(supply_frame, image=total_supply_icon,  bg='#5C62D6')
total_supply_label.pack(pady=10)
total_supply_label_text=Label(supply_frame, text='Total Suppliers', bg='#5C62D6', fg='white', font=('times new roman', 15, 'bold'))
total_supply_label_text.pack()
total_supply_label_count=Label(supply_frame, text='0', bg='#5C62D6', fg='white', font=('times new roman', 30, 'bold'))
total_supply_label_count.pack()

cat_frame=Frame(root, bg='#B8860B', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, height=170, width=280)
total_cat_icon=PhotoImage(file='totalcategorization.png')
total_cat_label=Label(cat_frame, image=total_cat_icon, bg='#B8860B')
total_cat_label.pack(pady=10)
total_cat_label_text=Label(cat_frame, text='Total Categories', bg='#B8860B', fg='white', font=('times new roman', 15, 'bold'))
total_cat_label_text.pack()
total_cat_label_count=Label(cat_frame, text='0', bg='#B8860B', fg='white', font=('times new roman', 30, 'bold'))
total_cat_label_count.pack()

product_frame=Frame(root, bg='#2E8B57', bd=3, relief=RIDGE)
product_frame.place(x=800, y=310, height=170, width=280)
total_product_icon=PhotoImage(file='totalproducts.png')
total_product_label=Label(product_frame, image=total_product_icon, bg='#2E8B57')
total_product_label.pack(pady=10)
total_product_label_text=Label(product_frame, text='Total Products', bg='#2E8B57', fg='white', font=('times new roman', 15, 'bold'))
total_product_label_text.pack()
total_product_label_count=Label(product_frame, text='0', bg='#2E8B57', fg='white', font=('times new roman', 30, 'bold'))
total_product_label_count.pack()

sale_frame=Frame(root, bg='#FF4500', bd=3, relief=RIDGE)
sale_frame.place(x=600, y=490, height=170, width=280)
total_sale_icon=PhotoImage(file='totalsales.png')
total_sale_label=Label(sale_frame, image=total_sale_icon, bg='#FF4500')
total_sale_label.pack(pady=10)
total_sale_label_text=Label(sale_frame, text='Total Sales', bg='#FF4500', fg='white', font=('times new roman', 15, 'bold'))
total_sale_label_text.pack()
total_sale_label_count=Label(sale_frame, text='0', bg='#FF4500', fg='white', font=('times new roman', 30, 'bold'))
total_sale_label_count.pack()





root.mainloop()

