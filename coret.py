from tkinter import *
from tkinter.filedialog import askopenfile 

window = Tk()
window.geometry("400x400")
window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")

key_gen_window = Frame(window)
key_gen_window.pack(side='top', pady=20)

parameter_sect = LabelFrame(key_gen_window, text='Parameter')
parameter_sect.place(relx=0.5, rely=0.5, anchor='center')

p_label = Label(parameter_sect, text='P: ')
p_label.grid(row=0, column=0)

p_entry = Entry(parameter_sect)
p_entry.grid(row=0, column=1)

window.mainloop()