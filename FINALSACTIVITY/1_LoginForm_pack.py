import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("400x300")
window.title("Login Form")

label = tk.Label(window, text="Login")
label.pack()

#Username
user_entry = tk.Entry(window,justify= CENTER)
user_entry.pack(pady=5)
user_entry.insert(0,"Username")

#Password
pass_entry = tk.Entry(window,justify= CENTER)
pass_entry.pack(pady=5)
pass_entry.insert(0,"Password")

#Login
login_button = tk.Button(window, text="Login", width=10, )
login_button.pack(pady=5)

#Remember Me
rbm_cb1 = tk.Checkbutton(window, text="Remember me")
rbm_cb1.pack(side= LEFT)

#Forget PW
forget_button = tk.Button(window, text="Forget Password", width=17 )
forget_button.pack(side= RIGHT)

#Create ACC
create_button = tk.Button(window, text="Create Account")
create_button.pack(side=BOTTOM)


window.mainloop()