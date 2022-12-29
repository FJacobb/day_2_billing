from tkinter import *
import time
from tkinter import messagebox
def message():
    bill = (float(total_bill_input.get()) + (
                float(total_bill_input.get()) * (float(percentage_input.get()) / 100))) / float(split_bill_input.get())
    messagebox.showinfo("split bill per person", message=f"Our of {split_bill_input.get()}, Each person will have to pay ${round(bill, 1)}")

def next():
    global split_bill_input, total_bill_input, percentage_input
    loading_text.destroy()
    frame = Frame(width=255, height=150, bg="#193751")
    frame.place(x=10, y=10)
    total_bill = Label(frame, text="What was the total bill? $", font=("arel", 7, "bold"), fg="#ffffff",bg="#193751")
    total_bill.place(x=10, y=10)
    total_bill_input = Entry(frame, width=25, fg="black", font=("arel", 9, "normal"))
    total_bill_input.place(x=10, y=25)
    split_bill = Label(frame, text="How many people do you want to split the bill with? ", font=("arel", 7, "bold"), fg="#ffffff",bg="#193751")
    split_bill.place(x=10, y=40)
    split_bill_input = Entry(frame, width=25, fg="black", font=("arel", 9, "normal"))
    split_bill_input.place(x=10, y=55)
    percentage = Label(frame, text="What percentage tip would you like to give?", font=("arel", 7,"bold"), fg="#ffffff",bg="#193751")
    percentage.place(x=10, y=70)
    percentage_input = Entry(frame, width=25, fg="black", font=("arel", 9, "normal"))
    percentage_input.place(x=10, y=85)
    Button(frame, text="Submit",fg="#ffffff", bg="#002145",  command=message).place(x=90, y=110)

home = Tk()
home.title("tip calculator")
home.geometry("450x250")
img = PhotoImage(file="image/25552 [Converted].png")
Label(home, image=img).place(x=0,y=0)
loading_text = Label(home, text="welcome to tip calculator", font=("arel", 20, "bold"), fg="#ffffff", bg="#002145")
loading_text.place(x=55, y=100)
home.after(4000, next)
home.mainloop()
