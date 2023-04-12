from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *

window = Tk()
window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")

# window.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a file", filetypes=("all files", "*.*"))

def open_file_dialog():
    file = filedialog.askopenfile(mode="r")
    if file is not None:
        print(file.name)

# Digital Signing Window
verify_window = Frame(window)
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

select_pri_button = Button(select_pri_sect, text='Select file', command=open_file_dialog)
select_pri_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

# Signature Type section
sign_type_sect = LabelFrame(verify_window, text='Signature Type')
sign_type_sect.grid(row=0, column=1, ipadx=30, ipady=40, padx=10)

r = IntVar()

Radiobutton(sign_type_sect, text="Signature in file      ", value=1, variable=r).grid(row=0, column=0)
Radiobutton(sign_type_sect, text="Separate signature", value=2, variable=r).grid(row=1, column=0)

# Select Signature section
select_signature_sect = LabelFrame(verify_window, text='Select Signature')
select_signature_sect.grid(row=1, column=1, ipadx=30, ipady=40, padx=10)

select_signature_sect_label = Label(select_signature_sect, text='No signature selected')
select_signature_sect_label.grid(row=0, column=0, pady=5)

select_pri_button = Button(select_signature_sect, text='Select file', command=open_file_dialog)
select_pri_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)

# Verify button
verify_button = Button(verify_window, text='Verify')
verify_button.grid(row=2, column=1, columnspan=2, ipadx=20, padx=10)

window.mainloop()