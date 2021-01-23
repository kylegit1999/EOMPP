from tkinter import *
from tkinter import messagebox
import mysql

mydb=mysql.connector.connect(user='lifechoices', passwd='@Lifechoices1234', database='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')

mycursor=mydb.cursor()



root = Tk()
root.title()
root.geometry("500x500")
root.configure(bg="cyan")

yep = Label(root, text='Enter Full Name')
yep.place(x=50, y=20)

passw = Label(root, text='Enter Password')
passw.place(x=50, y=50)

username = Entry(root, text= "Enter password")
username.place(x=250, y=20,width=100)

password = Entry(root, width=35)
password.place(x=250,y=50, width=100)


id = Label(root, text='Enter user ID')
id.place(x=50, y=85)

id = Label(root, text='Username')
id.place(x=50, y=115)

id = Entry(root, text= "Enter user ID")
id.place(x=250, y=110,width=100)

user = Entry(root, width=35)
user.place(x=250,y=82, width=100)




#regbtn =Button(root,text='Register', bg='yellow', command=verify)
#regbtn.place(x=150, y=135, width=150)


password.place(x=250,y=50, width=100)


def close():
    exit= messagebox.askyesno(title="?", message="Do you want to exit?")
    if exit ==True:
        root.destroy()
    else:
        return None

def validateLogin():
   messagebox.showinfo("you logged in ")


validateLogin= Button(root,text='Login', bg='lawngreen', command=validateLogin)
validateLogin.place(x=70, y=250, width=155)





exitbtn = Button(root, command=close, bg="blue" , text="exit")
exitbtn.place(x=70, y=250)


#logbtn = Button(root,text='Login', bg='yellow', command=log)
#logbtn.place(x=50, y=135, width=155)

root.mainloop()
