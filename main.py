import twilio.rest
import random
from tkinter import Tk, Label, Entry, Button, messagebox, Canvas

root = Tk()
root.title("OTP Verification")
root.geometry("600x550")

account_sid = ""
auth_token = ""

# Function to resend OTP
def resendOPT():
    global n
    n = random.randint(1000, 9999)  
    client = twilio.rest.Client(account_sid, auth_token)
    client.messages.create(to="", from_="", body=n)
    messagebox.showinfo("showinfo", f"OTP Sent: {n}")  

# Function to check OTP
def checkOTP():
    global n
    try:
        userInput = int(user_entry.get())  
        if userInput == n:
            messagebox.showinfo("showinfo", "Login Success")
            n = "done"  

        elif n == "done":
            messagebox.showinfo("showinfo", "OTP already entered")

        else:
            messagebox.showinfo("showinfo", "Wrong OTP")
    except ValueError:
        messagebox.showinfo("showinfo", "Invalid input")


c = Canvas(root, bg="white", width=400, height=300)
c.place(x=100, y=60)

login_label = Label(root, text="OTP Verification", font="bold")
login_label.place(x=210, y=90)


user_entry = Entry(root, borderwidth=2, width=30)
user_entry.place(x=190, y=160)

n = random.randint(1000, 9999)
client = twilio.rest.Client(account_sid, auth_token)
client.messages.create(to="", from_="", body=n)

submit_button = Button(root, text="Submit", command=checkOTP, font=('bold', 15))
submit_button.place(x=258, y=250)

resendButton = Button(root, text="Resend", command=resendOPT, font=("bold", 15))
resendButton.place(x=240, y=400)

root.mainloop()
