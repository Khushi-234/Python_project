import tkinter as tk
from tkinter import messagebox
import random

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
        exclude_characters = exclude_entry.get()
    except ValueError:
        messagebox.showerror(message="Please enter valid numeric inputs")
        return

    character_types = {
        'alphabets': alphabet_var.get(),
        'digits': digits_var.get(),
        'symbols': symbols_var.get()
    }

    valid_characters = ""
    if character_types['alphabets']:
        valid_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if character_types['digits']:
        valid_characters += "0123456789"
    if character_types['symbols']:
        valid_characters += "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    if not valid_characters:
        messagebox.showerror(message="Please select at least one character type")
        return

    if repeat == 1:
        password = random.sample(valid_characters, length)
    else:
        password = random.choices(valid_characters, k=length)

    if exclude_characters:
        password = [char for char in password if char not in exclude_characters]
        if len(password) < length:
            messagebox.showerror(message="Excluding characters has resulted in fewer options than requested. Please change the length or characters.")
            return

    password = ''.join(password)
    password_v.set(password)

def copy_password():
    password_gen.clipboard_clear()
    password_gen.clipboard_append(password_v.get())
    messagebox.showinfo("Success", "Password has been copied to clipboard.")


password_gen = tk.Tk()
password_gen.geometry("400x300")
password_gen.title("Password Generator")

title_label = tk.Label(password_gen, text="Password Generator", font=('Ubuntu Mono', 12))
title_label.pack(pady=10)

length_label = tk.Label(password_gen, text="Enter length of password:")
length_label.pack(pady=5)
length_entry = tk.Entry(password_gen, width=3)
length_entry.pack()

#Reapeatation button
repeat_label = tk.Label(password_gen, text="1: Repetition?\n2: No Repetition\nOtherwise:")
repeat_label.pack(pady=5)
repeat_entry = tk.Entry(password_gen, width=3)
repeat_entry.pack()

#Exclude character 
exclude_label = tk.Label(password_gen, text="Enter characters to exclude:")
exclude_label.pack(pady=5)
exclude_entry = tk.Entry(password_gen, width=3)
exclude_entry.pack()

#character types (letters, numbers, symbols). 
alphabet_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

alphabet_checkbox = tk.Checkbutton(password_gen, text="Include Alphabets", variable=alphabet_var)
alphabet_checkbox.pack()
digits_checkbox = tk.Checkbutton(password_gen, text="Include Digits", variable=digits_var)
digits_checkbox.pack()
symbols_checkbox = tk.Checkbutton(password_gen, text="Include Symbols", variable=symbols_var)
symbols_checkbox.pack()

#Generate button
password_button = tk.Button(password_gen, text="Generate Password", command=generate_password)
password_button.pack(pady=10)


password_v = tk.StringVar()
password_label_frame = tk.Frame(password_gen, bg="black")
password_label_frame.pack(pady=10)
password_label = tk.Entry(password_label_frame, bd=0, bg="light gray", textvariable=password_v, state="readonly")
password_label.pack()
password_label_frame.configure(bg="black")

#Copy password button
copy_button = tk.Button(password_gen, text="Copy Password", command=copy_password)
copy_button.pack(pady=5)

length_entry.configure(bg="light gray")
repeat_entry.configure(bg="light gray")
exclude_entry.configure(bg="light gray")
password_label.configure(bg="light gray")

password_gen.mainloop()
