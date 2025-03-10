from tkinter import *

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
leftFrame.place(x=0, y=120, width=200, height=555)
logo_Image = PhotoImage(file='logo.png')
imageLabel=Label(leftFrame, image=logo_Image)
imageLabel.pack()
menuLabel=Label(leftFrame, text="Menu", font=('times new roman', 20), bg='#212529', fg='#E0E0E0' )
menuLabel.pack(fill=X)


root.mainloop()

