import tkinter as tk
from tkinter import ttk
import mysql.connector as sql


def Database():
    global connect, cursor
    connect = sql.connect(user='root', host='localhost',
                          password='', database='residents')
    if connect.is_connected():
        print("successfully connected")
    cursor = connect.cursor()

    # cursor.execute("create table residents.resident(Name  varchar(25), age   int, date_of_birth date, " "gender
    # varchar(20), " "contact_no varchar(20), address varchar(20), aadhar_no varchar(20), first_dose_taken varchar(
    # 20), second_dose_taken varchar(20));")


from tkinter import *
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Python - vaccine Register Form")

width = 640
height = 620
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

# VARIABLES
name = tk.StringVar()
age = tk.StringVar()
date = tk.StringVar()
gender = tk.StringVar()
contact = tk.StringVar()
address = tk.StringVar()
aadhar_no = tk.StringVar()
first_dose = tk.StringVar()
second_dose = tk.StringVar()


# METHODS
def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure
             you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()



def Register():
    Database()
    if name.get()=="" or age.get() == "" or date.get() == ""
    or gender.get() == "" or contact.get() == "" or
    address.get() == "" or aadhar_no.get() == '' or
    first_dose.get() == "" or second_dose.get()=="":
        lbl_result.config(text="Please complete the required
        field!",fg="orange")
    else:
        cursor.execute("SELECT * FROM residents.resident WHERE
                       name = %s;",[name.get()])
        if cursor.fetchone() is not None:
            lbl_result.config(text="Username is already
                              taken", fg="red")
        else:
            cursor.execute(
                "INSERT INTO residents.resident(Name, age,
                 date_of_birth, gender, contact_no, address,
                 aadhar_no, first_dose_taken,
                 second_dose_taken)
                 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (str(name.get()), str(age.get()),
                 str(date.get()), str(gender.get()), 
                 str(contact.get()), str(address.get()),
                 str(aadhar_no.get()),str(first_dose.get()),  
                 str(second_dose.get())))
        connect.commit()
        name.set("")
        age.set("")
        date.set("")
        gender.set("")
        contact.set("")
        address.set("")
        aadhar_no.set('')
        first_dose.set("")
        second_dose.set("")
        lbl_result.config(text="Successfully Created!",
                          fg="green")
        cursor.close()
        connect.close()


# FRAMES
TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)

# LABEL WIDGETS
lbl_title = Label(TitleFrame, text="VACCINATION - Register Form", font=('arial', 12), bd=1, width=640)
lbl_title.pack()
lbl_name = Label(RegisterFrame, text="name:", font=('arial', 12), bd=18)
lbl_name.grid(row=1)
lbl_age = Label(RegisterFrame, text="age:", font=('arial', 12), bd=18)
lbl_age.grid(row=2)
lbl_date = Label(RegisterFrame, text="date of birth:", font=('arial', 12), bd=18)
lbl_date.grid(row=3)
lbl_gender = Label(RegisterFrame, text="gender:", font=('arial', 12), bd=18)
lbl_gender.grid(row=4)
lbl_contact = Label(RegisterFrame, text="contact number:", font=('arial', 12), bd=18)
lbl_contact.grid(row=5)
lbl_address = Label(RegisterFrame, text="address:", font=('arial', 12), bd=18)
lbl_address.grid(row=6)
lbl_aadhar_no = Label(RegisterFrame, text="aadhar number:", font=('arial', 12), bd=18)
lbl_aadhar_no.grid(row=7)
lbl_first_dose = Label(RegisterFrame, text="first dose taken:", font=('arial', 12), bd=18)
lbl_first_dose.grid(row=8)
lbl_second_dose = Label(RegisterFrame, text="second dose taken:", font=('arial', 12), bd=18)
lbl_second_dose.grid(row=9)
lbl_result = Label(RegisterFrame, text="", font=('arial', 12))
lbl_result.grid(row=10, columnspan=2)

# ENTRY WIDGETS
NAME = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=name, width=15)
NAME.grid(row=1, column=1)
AGE = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=age, width=15)
AGE.grid(row=2, column=1)
DATE = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=date, width=15)
DATE.grid(row=3, column=1)
GENDER = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=gender, width=15)
GENDER.grid(row=4, column=1)
CONTACT = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=contact, width=15)
CONTACT.grid(row=5, column=1)
ADDRESS = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=address, width=15)
ADDRESS.grid(row=6, column=1)
AADHAR_NO = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=aadhar_no, width=15)
AADHAR_NO.grid(row=7, column=1)
FIRST_DOSE = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=first_dose, width=15)
FIRST_DOSE.grid(row=8, column=1)
SECOND_DOSE = ttk.Entry(RegisterFrame, font=('arial', 12), textvariable=second_dose, width=15)
SECOND_DOSE.grid(row=9, column=1)

# BUTTON WIDGETS
btn_register = Button(RegisterFrame, font=('arial', 12), text="Register", command=Register)
btn_register.grid(row=10, columnspan=2)

# MENUBAR WIDGETS
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# INITIALIZATION
if __name__ == '__main__':
    root.mainloop()
