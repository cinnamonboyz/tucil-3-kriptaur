import os
from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *

from RSA import sign_in_file, sign_separate_file
from util import read_key_file

# sign_window = Tk()
# sign_window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")

private_key = None
plain_file = None
def digital_sign():
    sign_window = Toplevel()

    def open_file_dialog():
        global plain_file
        
        file = filedialog.askopenfile(mode='rb')
        
        if file:
            plain_file = file
            select_file_sect_label.config(text=os.path.abspath(file.name))

    def open_pri_dialog():
        global private_key
        file = filedialog.askopenfile(mode="r", filetypes=[("PRI Files", "*.pri")])
        if file:
            private_key = read_key_file(os.path.abspath(file.name))
            select_pri_sect_label.config(text=os.path.abspath(file.name))

    # Digital Signing Window
    digital_signing_window = Frame(sign_window)
    digital_signing_window.grid(row=0, column=0, padx=10, pady=20)

    # Select File section
    select_file_sect = LabelFrame(digital_signing_window, text='Select File')
    select_file_sect.grid(row=0, column=0, ipadx=30, ipady=40, padx=10)

    select_file_sect_label = Label(select_file_sect, text='No file selected')
    select_file_sect_label.grid(row=0, column=0, pady=5)

    select_file_button = Button(select_file_sect, text='Select file', command=open_file_dialog)
    select_file_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

    # Select Private Key section
    select_pri_sect = LabelFrame(digital_signing_window, text='Select Private Key')
    select_pri_sect.grid(row=1, column=0, ipadx=30, ipady=40, padx=10)

    select_pri_sect_label = Label(select_pri_sect, text='No file selected')
    select_pri_sect_label.grid(row=0, column=0, pady=5)

    select_pri_button = Button(select_pri_sect, text='Select file', command=open_pri_dialog)
    select_pri_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

    # Signature Type section
    sign_type_sect = LabelFrame(digital_signing_window, text='Signature Type')
    sign_type_sect.grid(row=0, column=1, ipadx=30, ipady=40, padx=10)

    r = IntVar(value=1)

    radio_button_in_file = Radiobutton(sign_type_sect, text="Signature in file      ", value=1, variable=r)
    radio_button_in_file.grid(row=0, column=0)
    radio_button_separate_file = Radiobutton(sign_type_sect, text="Separate signature", value=2, variable=r)
    radio_button_separate_file.grid(row=1, column=0)

    def sign_file():
        if r.get() == 1:
            p = Path(plain_file.name)
            if p.suffix != '.txt':
                messagebox.showerror('Error', 'Please use seperate signature for non-.txt files')
                return
            
            buf = sign_file(plain_file, private_key)
            save_path = f'./signed_files/signed_{p.stem + p.suffix}'
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'wb') as signed_file:
                signed_file.write(buf.getvalue())

            messagebox.showinfo('Info', 'File signed!')
        else:
            p = Path(plain_file.name)
            save_path = f'./signature/{p.stem + p.suffix}_signature.txt'
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'w') as signature_file:
                buf = sign_separate_file(plain_file, private_key)
                signature_file.write(buf.getvalue())

            messagebox.showinfo('Info', 'Signature created!')
        
            

    # Sign button
    signature_button = Button(digital_signing_window, text='Sign', command=sign_file)
    signature_button.grid(row=1, column=1, columnspan=2, ipadx=20, padx=10)

    # sign_window.mainloop()