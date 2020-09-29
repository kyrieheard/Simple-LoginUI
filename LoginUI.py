from Tkinter import *

root = Tk()


users = {}
status = ""

root.title('EDMUNDS-12')

label1 = Label(root, text=" Login Or Sign-up", width=25,)     # MENU
label1.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=35, borderwidth=5)     # TEXT BOX 1 (USERNAME)
e.grid(row=1, column=0, columnspan=2)
e.insert(0, 'Username')

f = Entry(root, width=35, borderwidth=5)     # TEXT BOX 2 (PASSWORD)
f.grid(row=2, column=0, columnspan=2)
f.insert(0, 'Password')


def signclick():     # COMMAND FOR SIGNUP BUTTON
    createuser =e.get()
    if createuser in users:
        l1 = Label(root, text="Username taken", padx=50)
        l1.grid(row=0, column=0, columnspan=2)
    else:
        createpass = f.get()
        users[createuser] = createpass
        l3 = Label(root, text="Account created, please Login.")
        l3.grid(row=0, column=0, columnspan=2)


def logclick():     # COMMAND FOR LOGIN BUTTON
    loguser = e.get()
    logpass = f.get()
    if loguser in users and users[loguser] == logpass:
        l2 = Label(root, text="Login Successful", padx=50)
        l2.grid(row=0, column=0, columnspan=2)
    else:
        l2 = Label(root, text="Wrong Username and Password")
        l2.grid(row=0, column=0, columnspan=2)


button_1 = Button(root, text='  Login  ', bg='white', fg='black', command=logclick)
button_1.grid(row=3, column=1)
# LOGIN BUTTON (RIGHT BUTTON ON THE BOTTOM)

button_2 = Button(root, text='Sign-up', bg='white', fg='black', command=signclick)
button_2.grid(row=3, column=0)
# SIGN UP BUTTON (LEFT BUTTON ON THE BOTTOM)

root.mainloop()
