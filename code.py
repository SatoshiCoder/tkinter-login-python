from tkinter import *
from functools import partial

def validateLogin(username, password,linkname):
	print("username entered :", username.get())
	print("password entered :", password.get())
	print("link facebook :", linkname.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Auto facebook')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

linknameLabel = Label(tkWindow, text="Link facebook").grid(row=2, column=0)
linkname = StringVar()
linknameEntry = Entry(tkWindow, textvariable=linkname).grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password,linkname)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()
