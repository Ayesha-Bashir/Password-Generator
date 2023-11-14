
# Phase_1_Task2

from tkinter import *
import string
import random

import pyperclip


def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordField.insert(0, random.sample(small_alphabets, password_length))

    if choice.get() == 2:
        passwordField.insert(0, random.sample(small_alphabets + capital_alphabets, password_length))

    if choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.title('Password Generator')
root.config(bg='RosyBrown4')
choice = IntVar()
root.wm_geometry('300x380')
Font = ('arial', 13, 'bold')

passwordLabel = Label(root, text=' Password Generator', font=('Time New Roman', 20, 'bold'), bg='gray20', fg='white')
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice, font=Font)
weakradioButton.config(bg='honeydew2')
weakradioButton.grid(pady=5)

mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.config(bg='honeydew2')
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice, font=Font)
strongradioButton.config(bg='honeydew2')
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text='Password Length', font=Font,bg='gray20', fg='white')
lengthLabel.grid()

length_Box = Spinbox(root, from_=5, to_=10, width=5, font=Font)
length_Box.grid()

generateButton = Button(root, text='Generate', font=Font, command=generator)
generateButton.config(bg='honeydew2')
generateButton.grid(pady=5)

passwordField = Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

copyButton = Button(root, text='Copy', font=Font, command=copy)
copyButton.config(bg='honeydew2')
copyButton.grid(pady=5)

root.mainloop()