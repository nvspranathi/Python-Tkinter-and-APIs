import tkinter as tk
from tkinter import messagebox,ttk
import tkinter.ttk
from openpyxl import load_workbook

root = tk.Tk()
file_path = r"students_form.xlsx"
A = load_workbook(file_path)
B = A["Registration"]

def OnClick_Submit():
    name = name_textbox.get()
    email = email_textbox.get()
    phone = Phone_textbox.get()
    branch = branch_dropdown.get()
    agree = agree_value.get()


    if name and email and phone and agree==1:
        B.append([name,email,phone,branch,agree])
        A.save(file_path)
        messagebox.showinfo("Status","Data Submitted")
    else:
        messagebox.showinfo("Warning","Please Fill all the Fields")


root.geometry("300x400")
root.configure(bg="#ADD8E6")
root.title("Student Registration form")

name_label = tk.Label(root,text="Enter Name")
name_label.pack(anchor=tk.W,padx=10) # anchor=tk.W says align towards west
name_textbox = tk.Entry(root) # to take the input, entry is an empty space that will be seen on UI
name_textbox.pack(anchor=tk.W,padx=10)

email_label = tk.Label(root,text="Enter Email")
email_label.pack(anchor=tk.W,padx=10)
email_textbox = tk.Entry(root)
email_textbox.pack(anchor=tk.W,padx=10)

Phone_label = tk.Label(root,text="Enter Phone Number")
Phone_label.pack(anchor=tk.W,padx=10)
Phone_textbox = tk.Entry(root)
Phone_textbox.pack(anchor=tk.W,padx=10)

# for a dropdown
choices = ['CS','EC','Mechanical']
branch_label = tk.Label(root,text='Select a branch')
branch_label.pack(anchor=tk.W,padx=10)
branch_dropdown = ttk.Combobox(root,values=choices) #theme_tkinter -> ttk module
branch_dropdown.pack(anchor=tk.W,padx=10)

# for checkbox
agree_value = tkinter.IntVar() #uncheck=0 check=1
agree_checkbox = ttk.Checkbutton(root,text='Do you agree with Terms and Conditions',variable=agree_value)
agree_checkbox.pack(anchor=tkinter.W,padx=10,pady=5)

submit_button = tk.Button(root,text="SUBMIT",command=OnClick_Submit)
submit_button.pack(anchor=tk.W,padx=10)

root.mainloop()