from tkinter import *
from tkinter.filedialog import askopenfile 

window = Tk()
window.geometry("400x400")
window.title("Open File Dialog Example")

def open_file_dialog():
    file = askopenfile(mode="")
    if file is not None:
        print(file.name)

open_button = Button(window, text="Open File", command=open_file_dialog)
open_button.pack(pady=20)

window.mainloop()
