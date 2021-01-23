import mysql.connector
import tkinter as tk
from tkinter import  messagebox

mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')

mycursor=mydb.cursor()


window = tk.Tk()
window.title()
window.geometry("500x500")
window.configure(bg="yellow")


def verify():
    user_verification = username.get()
    pass_verification = password.get()
    sql = "SELECT * FROM Login WHERE username= %s and Password = %s"
    mycursor.execute(sql, [(user_verification), (pass_verification)])
    results= mycursor.fetchall()



    if results:
        for i in results:
            logged()
            break

    else:
            failed()

def logged():
    messagebox.showinfo("You have logged in")

def failed():

    messagebox.showinfo("Try again")

# def failed():
#     messagebox.showinfo("Press to Exit")




yep = tk.Label(window, text='Enter username')
yep.place(x=50, y=20)

passw = tk.Label(window, text='Enter password')
passw.place(x=50, y=50)

username = tk.Entry(window, text= "Enter password")
username.place(x=250, y=20,width=100)

password = tk.Entry(window, width=35)
password.place(x=250,y=50, width=100)

logbtn = tk.Button(window,text='Login', bg='purple', command=verify)
logbtn.place(x=50, y=135, width=155)

# regbtn = tk.Button(window,text='Register', bg='blue', command=verify)
# regbtn.place(x=180, y=135, width=150)

def close():
    exit= messagebox.askyesno(title="?", message="Do you want to exit?")
    if exit ==True:
        window.destroy()
    else:
        return None

exitbtn = tk.Button(window, command=close, bg="blue" , text="exit")
exitbtn.place(x=209, y=135)


window.mainloop()
