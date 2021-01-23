from tkinter import *
from tkinter import messagebox
import mysql.connector

root = Tk()
root.title()
root.geometry("500x500")
root.configure(bg="grey")

mydb=mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', database='lifechoicesonline', host='127.0.0.1', auth_plugin='mysql_native_password')

mycursor=mydb.cursor()

def verify():
    try:
        id_verification = id.get()
        name_verification = fname.get()
        user_verification = use.get()
        pass_verification = password.get()
        sql = "INSERT INTO Register(id,full_name,username,password) VALUES(%s,%s,%s,%s)"
        valu=(id_verification,name_verification,user_verification,pass_verification)
        mycursor.execute(sql,valu)
        mydb.commit()
        messagebox.showinfo("successfully created")
    except ValueError as i:
        print(i)
        messagebox.showinfo("user already exists")


yep = Label(root, text='Enter Full Name')
yep.place(x=50, y=20)

passw = Label(root, text='Enter Password')
passw.place(x=50, y=50)

fname = Entry(root, text= "Enter password")
fname.place(x=250, y=20,width=100)
#
password = Entry(root, width=35)
password.place(x=250,y=50, width=100)


lid= Label(root, text='Enter user ID')
lid.place(x=50, y=85)

user = Label(root, text='Cell number')
user.place(x=50, y=115)

id = Entry(root)
id.place(x=250, y=85,width=100)
#
use = Entry(root, width=35)
use.place(x=250,y=115, width=100)






register = Button(root,text='Login', bg='red', command= verify)
register.place(x=250, y=250, width=155)

def close():
    exit= messagebox.askyesno(title="?", message="Do you want to exit?")
    if exit ==True:
        root.destroy()
    else:
        return None




#regbtn =Button(root,text='Register', bg='yellow', command=verify)
#regbtn.place(x=150, y=135, width=150)

#import staff as reg


# password.place(x=250,y=50, width=100)
label_4 = Label(root, text= "Gender",width=10,font=("bold", 10))
label_4.place(x=50,y=150)
var = IntVar()
Radiobutton(root, text="Male", padx = 20, variable=var, value=1 , bg="yellow").place(x=250, y= 150)
Radiobutton(root, text="female",padx = 20, variable=var, value=2,bg="red").place(x=350, y=150)

exitbtn = Button(root, command=close, bg="blue" , text="exit")
exitbtn.place(x=70, y=250)



#logbtn = tk.Button(root,text='Login', bg='yellow', command=)#
#logbtn.place(x=50, y=135, width=155)#
root.mainloop()
