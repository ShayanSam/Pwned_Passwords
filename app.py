
import tkinter as tk
import tkinter.messagebox
from tkinter.ttk import *
from checkmypass import main

root = tk.Tk()
root.title("Pwned Passwords")


# setting the windows size
root.geometry("400x100")
root.config(bg='#808080')

# declaring string variable
passw_var = tk.StringVar()


# defining a function that will
# Create a messagebox showinfo
def onClick(main):
    if main:
        tkinter.messagebox.showinfo(
            message="your password was NOT found. Carry on!")
    else:
        tkinter.messagebox.showwarning(
            message="you should probably change your password!")


def submit():
    password = passw_var.get()
    onClick(main(password))
    passw_var.set("")


# creating a label for password
passw_label = tk.Label(root, text='Enter your password ',
                       font=('calibre', 10, 'bold'), bg='#808080')

# creating a entry for password
passw_entry = tk.Entry(root, textvariable=passw_var,
                       font=('calibre', 15, 'normal'), show='*')

passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)


# Create style Object
style = Style()

style.configure('TButton', font=('calibri', 15, 'bold'),
                borderwidth='4')

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])

# button 1
btn1 = Button(root, text='Quit !', command=quit,
              width=6)
btn1.grid(row=2, column=0, padx=10)

# button 2
btn2 = Button(root, text='Pwned ?', command=submit, width=8)
btn2.grid(row=2, column=1, padx=10)


# performing an infinite loop
# for the window to display
root.mainloop()
