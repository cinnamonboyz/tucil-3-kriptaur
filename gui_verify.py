import os
from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *

from RSA import verify_in_file, verify_separate_file
from util import read_key_file

# verify_window = Tk()
# verify_window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")
public_key = None
signed_file = None
signature_file = None
def digital_verify():
    verify_window = Toplevel()

    def open_file_dialog():
        global signed_file

        file = filedialog.askopenfile(mode='rb')
        if file:
            signed_file = file
            select_file_sect_label.config(text=os.path.abspath(file.name))

    def open_pub_dialog():
        global public_key

        file = filedialog.askopenfile(mode="r", filetypes=[("PUB Files", "*.pub")])
        if file:
            public_key = read_key_file(os.path.abspath(file.name))
            select_pri_sect_label.config(text=os.path.abspath(file.name))
            
    def open_signature_dialog():
        global signature_file

        file = filedialog.askopenfile(mode="r", filetypes=[("Signature Files", "*.txt")])
        if file:
            signature_file = file
            select_signature_sect_label.config(text=os.path.abspath(file.name))

    # Digital Verifying Window
    verify_window = Frame(verify_window)
    verify_window.grid(row=0, column=0, padx=10, pady=20)

    # Select File section
    select_file_sect = LabelFrame(verify_window, text='Select File')
    select_file_sect.grid(row=0, column=0, ipadx=30, ipady=40, padx=10)

    select_file_sect_label = Label(select_file_sect, text='No file selected')
    select_file_sect_label.grid(row=0, column=0, pady=5)

    select_file_button = Button(select_file_sect, text='Select file', command=open_file_dialog)
    select_file_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

    # Select Public Key section
    select_pri_sect = LabelFrame(verify_window, text='Select Public Key')
    select_pri_sect.grid(row=1, column=0, ipadx=30, ipady=40, padx=10)

    select_pri_sect_label = Label(select_pri_sect, text='No file selected')
    select_pri_sect_label.grid(row=0, column=0, pady=5)

    select_pri_button = Button(select_pri_sect, text='Select file', command=open_pub_dialog)
    select_pri_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

    # Signature Type section
    sign_type_sect = LabelFrame(verify_window, text='Signature Type')
    sign_type_sect.grid(row=0, column=1, ipadx=30, ipady=40, padx=10)

    r = IntVar(value=1)

    def check_radio():
        if r.get() == 1:
            select_signature_sect.grid_remove()
        else:
            select_signature_sect.grid(row=1, column=1, ipadx=30, ipady=40, padx=10)

    radio_button_in_file = Radiobutton(sign_type_sect, text="Signature in file      ", value=1, variable=r, command=check_radio)
    radio_button_in_file.grid(row=0, column=0)
    radio_button_separate_file = Radiobutton(sign_type_sect, text="Separate signature", value=2, variable=r, command=check_radio)
    radio_button_separate_file.grid(row=1, column=0)

    # Select Signature section
    select_signature_sect = LabelFrame(verify_window, text='Select Signature')

    select_signature_sect_label = Label(select_signature_sect, text='No signature selected')
    select_signature_sect_label.grid(row=0, column=0, pady=5)

    select_pri_button = Button(select_signature_sect, text='Select file', command=open_signature_dialog)
    select_pri_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

    def verify():
        try:
            if r.get() == 1:
                verified = verify_in_file(signed_file, public_key)
            else:
                verified = verify_separate_file(signed_file, signature_file, public_key)
        except Exception as e:
            return messagebox.showwarning('Info', f'File is not verified!, {e}')

        if verified:
            messagebox.showinfo('Info', 'File is verified!')
        else:
            messagebox.showwarning('Info', 'File is not verified!')


    # Verify button
    verify_button = Button(verify_window, text='Verify', command=verify)
    verify_button.grid(row=2, column=0, columnspan=2, ipadx=20, padx=10, pady=5)

    # verify_window.mainloop()