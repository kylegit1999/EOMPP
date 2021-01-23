import mysql.connector
import tkinter as tk
from tkinter import  messagebox


mydb=mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', database='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')

mycursor=mydb.cursor()



window = tk.Tk()
window.title("option")
window.geometry("500x500")
window.configure(bg="purple")
def stud():
    import login
    login.login()

def admin():
    import admin
    admin.mainloop()

# def staff():
#     import staff
#     staff.mainloop()

def register():
    import register
    register.mainloop()
import tkinter as tk
from tkinter import  messagebox

def table():
    import table
    table.mainloop()

# def stud():
#     import students
#     students.mainloop()
#):
#     import students
#     students.mainloop()
#
# def admin():
#     import admin
#     admin.mainloop()
# def admin():
#     import admin
#     admin.mainloop()
#
# def staff():
#     import staff
#     staff.mainloop()
#
# def register():
#     import register
#     register.mainloop()

stud_btn = tk.Button(window, text="Login", command=stud, bg='grey', fg='black')
stud_btn.grid(row=6, column=2)

admin_btn = tk.Button(window, text="Admin", command=admin, bg='grey', fg='black')
admin_btn.grid(row=7, column=3)

# staff_btn = tk.Button(window, text="Staff", command=stud, bg='grey', fg='black')
# staff_btn.grid(row=8, column=4)

reg_btn = tk.Button(window, text="Register", command=register, bg='grey', fg='black')
reg_btn.grid(row=9, column=6)

table_btn = tk.Button(window, text="login record", command=table, bg='grey', fg='black')
table_btn.grid(row=10, column=7)


def close():
    exit= messagebox.askyesno(title="?", message="Do you want to exit?")
    if exit ==True:
        window.destroy()
    else:
        return None

exitbtn =  tk.Button(window, command=close, bg="blue" , text="exit")
exitbtn.place(x=230, y=150)

window.mainloop()
