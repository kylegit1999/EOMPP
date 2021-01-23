import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import  messagebox


window = tk.Tk()
window.title()
window.geometry("500x500")
window.configure(bg="purple")

mydb=mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', database='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM Register")
results = mycursor
i = 0
if results:
    for x in results:
        for v in range(len(x)):
            e = tk.Entry(window, width=20)
            e.grid(row=i, column=v)
            e.insert(END, x[v])
        i=i+1

def close():
    exit= messagebox.askyesno(title="?", message="Do you want to exit?")
    if exit ==True:
        window.destroy()
    else:
        return None

def clear():
    mycursor.execute("TRUNCATE TABLE Register")
    messagebox.showinfo("Delete", "ALL register User Deleted")
    window.destroy()

exitbtn =  tk.Button(window, command=close, bg="blue" , text="exit")
exitbtn.place(x=230, y=150)

clearbtn =  tk.Button(window, command=clear, bg="blue" , text="clear")
clearbtn.place(x=230, y=200)

window.mainloop()
