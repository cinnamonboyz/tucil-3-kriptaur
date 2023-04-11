# from key_generator import get_random_key
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 


window = Tk()
window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")

# key gen window
key_gen_window = Frame(window)
key_gen_window.grid(row=0, column=0, padx=10, pady=10)


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

random_button = Button(parameter_sect, text='Randomize parameters')
random_button.grid(row=3, column=0, columnspan=2, ipadx=20, padx=10)


# save key section
save_key_sect = LabelFrame(key_gen_window, text='Save key')
save_key_sect.grid(row=0, column=1, ipadx=30, ipady=40, padx=10)

key_name_label = Label(save_key_sect, text='Enter the key name')
key_name_label.grid(row=0, column=0, pady=5)

key_name_entry = Entry(save_key_sect)
key_name_entry.grid(row=1, column=0, pady=10, padx=15)

save_key_button = Button(save_key_sect, text='Generate & save key')
save_key_button.grid(row=2, column=0, pady=5, ipadx=15)

window.mainloop()
