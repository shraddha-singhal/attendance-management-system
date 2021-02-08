from tkinter import *
from tkinter import ttk
import os

class xyz:
    user='admin'
    passw='admin'

    def __init__(self,root):

        self.root=root
        self.root.title('LOGIN SCREEN')

        Label(text='Username',font='Times 15').grid(row=1,column=1,pady=20)
        self.username=Entry()
        self.username.grid(row=1,column=2,columnspan=10)

        
        Label(text='Password',font='Times 15').grid(row=2,column=1,pady=20)
        self.password=Entry(show='*')
        self.password.grid(row=2,column=2,columnspan=10)

        ttk.Button(text='LOGIN',command=self.login_user).grid(row=3,column=2)

    def login_user(self):
        if self.username.get()==self.user and self.password.get()==self.passw:
            root.destroy()

            os.system(r"python C:\Users\aggar\Desktop\Face-Recognition-Based-Attendance-System-master\train.py")
        else:
            self.message=Label(text='Username or password is incorrect.Try Again',fg='Red')
            self.message.grid(row=6,column=2)

if __name__=='__main__':
    root=Tk()
    root.geometry('425x225')
    application=xyz(root)

    root.mainloop()
