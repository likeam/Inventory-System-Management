from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employees import connectDatabase



def salesForm(root):
    categoryFrame=Frame(root, width=1070, height=567)
    categoryFrame.place(x=200, y=105)

    headingLabel= Label(categoryFrame,text="Manage Sales Details", font=('times new roman', 15, 'bold'),  bg='#212529', fg='#E0E0E0')
    headingLabel.place(x=0, y=0,  relwidth=1)

    backButton = Button(categoryFrame, text="Back", padx=20,pady=10, font=('times new roman', 15, 'bold'),cursor="hand2", bg='#9E9E9E', command=lambda : categoryFrame.place_forget())
    backButton.place(x=10, y=30)