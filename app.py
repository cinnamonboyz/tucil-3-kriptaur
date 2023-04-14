import os
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from key_generator import get_random_key
from RSA import generate_private_key, generate_public_key
from util import is_prime, is_relative_prime, write_key_file
from gui_sign import digital_sign
from gui_verify import digital_verify

window = Tk()
window.title("II4031 - Cryptography and Coding")

def gen_key():
    top = Toplevel(window)

    # key gen window
    key_gen_window = Frame(top)
    key_gen_window.grid(row=0, column=0, padx=10, pady=20, columnspan=3)


    # parameter section
    parameter_sect = LabelFrame(key_gen_window, text='Parameter')
    parameter_sect.grid(row=0, column=0, ipadx=30, ipady=40, padx=10)

    p_label = Label(parameter_sect, text='p : ')
    p_label.grid(row=0, column=0)

    p_entry = Entry(parameter_sect)
    p_entry.grid(row=0, column=1, pady=5)

    q_label = Label(parameter_sect, text='q : ')
    q_label.grid(row=1, column=0)

    q_entry = Entry(parameter_sect)
    q_entry.grid(row=1, column=1, pady=5)

    e_label = Label(parameter_sect, text='e : ')
    e_label.grid(row=2, column=0)

    e_entry = Entry(parameter_sect)
    e_entry.grid(row=2, column=1, pady=5)

    def randomize_params():
        p, q, e = get_random_key()

        p_entry.delete(0, END)
        p_entry.insert(0, p)

        q_entry.delete(0, END)
        q_entry.insert(0, q)

        e_entry.delete(0, END)
        e_entry.insert(0, e)

    random_button = Button(parameter_sect, text='Randomize parameters', command=randomize_params)
    random_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)


    # save key section
    save_key_sect = LabelFrame(key_gen_window, text='Save key')
    save_key_sect.grid(row=0, column=1, ipadx=30, ipady=52, padx=10)

    key_name_label = Label(save_key_sect, text='Enter the key name')
    key_name_label.grid(row=0, column=0, pady=5)

    key_name_entry = Entry(save_key_sect)
    key_name_entry.grid(row=1, column=0, pady=10, padx=15)

    def save_key():
        p = int(p_entry.get())
        q = int(q_entry.get())
        e = int(e_entry.get())

        if not is_prime(p) or not is_prime(q):
            messagebox.showerror("Error", "p or q must be a prime number!")
            return

        if not is_relative_prime((p - 1)*(q - 1), e):
            messagebox.showerror('Error', 'Totien n and e must b relative prime!')
            return

        public_key = generate_public_key(p, q, e)
        private_key = generate_private_key(p, q, e)

        write_key_file(public_key, f'./keys/{key_name_entry.get()}.pub')
        write_key_file(private_key, f'./keys/{key_name_entry.get()}.pri')

        messagebox.showinfo('Info', 'Key generated successfully!')

    save_key_button = Button(save_key_sect, text='Generate & save key', command=save_key)
    save_key_button.grid(row=2, column=0, pady=5, ipadx=15)


navbar = Frame(window)
navbar.grid(row=1, column=0, pady=20)

title_label = Label(window, text='Tugas Kecil 3 - Digital Signature Program', font=('TkDefaultFont', 14, 'bold'))
title_label.grid(row=0, pady=5, padx=10)

info_label_1 = Label(window, text='by')
info_label_1.grid(row=2, column=0)
info_label_2 = Label(window, text='Fikri Muhammad Fahreza')
info_label_2.grid(row=3, column=0)
info_label_3 = Label(window, text='Aldi Fadlian Sunan')
info_label_3.grid(row=4, column=0)

key_gen_button = Button(navbar, text='Generate Key', width=20, command=gen_key)
key_gen_button.grid(row=0, column=0, padx=100, pady=10)
sign_button = Button(navbar, text='Sign', width=20, command=digital_sign)
sign_button.grid(row=1, column=0, padx=100, pady=10)
verify_button = Button(navbar, text='Verify', width=20, command=digital_verify)
verify_button.grid(row=2, column=0, padx=100, pady=10)

window.mainloop()