from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk

class BANK:
    def __init__(self, root, account_number):
        self.root = root
        self.account_number = account_number
        self.withdraw_limit = 20000
        self.deposit_limit =  20000

        self.root.title("WELCOME TO BHARAT BANK")
        self.frame = tk.Frame(root, bg="navy blue")
        self.frame.pack(fill="both", expand=True)

        new_label = Label(root, text="THANK YOU VERY MUCH FOR CHOOSING OUR BHARAT BANK!")
        new_label.pack()

        self.balance = 1000

        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}")
        self.balance_label.place(x=500,y=200)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.place(x=400,y=300)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.place(x=600,y=300)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.place(x=350,y=400)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.place(x=700,y=400)

        btn_logout = Button(root, text="Logout", font='Verdana 10 bold', command=self.clear_fields)
        btn_logout.place(x=900, y=100)

    def withdraw(self):
        amount = self.get_amount()
        if amount <= 0 or amount > self.balance or amount > self.withdraw_limit:
            messagebox.showerror("Invalid Amount", "Invalid withdrawal amount.")
            return

        self.balance -= amount
        self.update_balance_label()

    def deposit(self):
        amount = self.get_amount()
        if amount <= 0 or amount > self.deposit_limit:
            messagebox.showerror("Invalid Amount", "Invalid deposit amount.")
            return

        self.balance += amount
        self.update_balance_label()

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            return amount
        except ValueError:
            return 0

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def clear_fields(self):
        accnoentry.delete(0, END)
        userentry.delete(0, END)
        passentry.delete(0, END)
        self.root.destroy()

def open_new_window(account_number):
    bank_window = Toplevel(main)
    bank_app = BANK(bank_window, account_number)

def submit():
    if accnoentry.get() == "" or userentry.get() == "" or passentry.get() == "":
        messagebox.showerror("Error", "Enter User Name, Account number, and Password")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="Bharat@123#", database="usersinfo")
            cur = con.cursor()

            cur.execute("select * from users  WHERE BINARY username=%s and password = %s and account_number=%s",
                        (userentry.get(), passentry.get(), accnoentry.get()))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Credentials")
            else:
                messagebox.showinfo("Success", "Successfully Login")
                open_new_window(accnoentry.get())

            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to: {str(es)}")

main = Tk()
main.geometry("900x900")
main.title("BHARAT BANK")
frame = tk.Frame(main, bg="purple")
frame.pack(fill="both", expand=True)
heading = Label(main,text="WELCOME TO BHARAT BANK ",font="italic 20 bold",bg='blue',fg='grey')
heading.place(x=450,y=100)
user_name = StringVar()
account_number = StringVar()
password = StringVar()
account_number=Label(main,text="ACCOUNT NUMBER ",font="italic 10 bold",bg='sky blue',fg='black')
user_name = Label(main,text="USER NAME",font="italic 10 bold",bg='sky blue',fg='black')
password = Label(main,text="PASSWORD",font="italic 10 bold",bg='sky blue',fg='black')
account_number.place(x=400,y=300)
user_name.place(x=400,y=350)
password.place(x=400,y=400)
accnoentry = Entry(main,textvariable=account_number,width=40)
accnoentry.place(x=600,y=300)
userentry=Entry(main,textvariable=user_name,width=40)
userentry.place(x=600,y=350)
passentry=Entry(main,textvariable=password,width=40, show='*')
passentry.place(x=600,y=400)
image = Image.open("C:\\Users\\BHARATH & HARI\\Desktop\\images\\bank.png")  # Replace "bank_logo.png" with your image file
photo = ImageTk.PhotoImage(image)

# Create a Label to display the image
image_label = tk.Label(main, image=photo)
image_label.place(x=100, y=100)  # Adjust the placement as needed

image_label2 = tk.Label(main, image=photo)
image_label2.place(x=1100, y=100)


def move_text():
    global text_x, text_id

    canvas.move(text_id, 1, 0)
    text_x += 1

    if text_x > canvas.winfo_width():
        canvas.move(text_id, -canvas.winfo_width(), 0)
        text_x -= canvas.winfo_width()

    canvas.after(10, move_text)

canvas = tk.Canvas(main, width=400, height=100, bg='red')
canvas.pack()
text = "THANKS FOR CHOOSING BHARAT BANK"
text_id = canvas.create_text(0, 50, text=text, anchor="w")
text_x = 0
move_text()

btn_login = Button(main, text="Submit", font='Verdana 10 bold', command=submit)
btn_login.place(x=650, y=493)

main.mainloop()
