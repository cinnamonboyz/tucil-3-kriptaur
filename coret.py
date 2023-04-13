# from tkinter import *
# from tkinter.filedialog import askopenfile 

# window = Tk()
# window.geometry("400x400")
# window.title("Open File Dialog Example")

# def open_file_dialog():
#     file = askopenfile(mode="")
#     if file is not None:
#         print(file.name)

# open_button = Button(window, text="Open File", command=open_file_dialog)
# open_button.pack(pady=20)

# window.mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()

messagebox.showinfo("showinfo", "Information")

messagebox.showwarning("showwarning", "Warning")

messagebox.showerror("showerror", "Error")

messagebox.askquestion("askquestion", "Are you sure?")

messagebox.askokcancel("askokcancel", "Want to continue?")

messagebox.askyesno("askyesno", "Find the value?")

messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()
