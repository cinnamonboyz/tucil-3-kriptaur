from tkinter import *
from tkinter.filedialog import askopenfile 

window = Tk()
window.title("Tugas Kecil 3 - Program Tanda-tangan Digital")


greeting = Label(window, text="Digital Signer", font=("San Francisco", 18, "bold"))
greeting.pack()

frame1 = LabelFrame(window, text="Pilih File", font=("Helvetica 14 bold"), padx=10, pady=10)
frame1.pack(padx=10, pady=10)
frame1_desc = Label(frame1, text="Tidak ada file dipilih")
frame1_desc.pack()

entry = Entry(frame1, width=40)
entry.pack()
entry.get()


def myClick():
    myLabel = Label(frame1, text=entry.get())
    myLabel.pack()

button1 = Button(frame1, text="Pilih File", padx=40, command=myClick)
button1.pack()


frame2 = LabelFrame(window, width=50, text="Pilih Kunci Privat", font="Helvetica 14 bold", padx=10, pady=10)
frame2.pack(padx=20, pady=20)
frame2_desc = Label(frame2, text="Tidak ada kunci privat dipilih")
frame2_desc.pack()

button2 = Button(frame2, text="Pilih File", padx=40, command=myClick)
button2.pack()

frame3 = LabelFrame(window, width=50, text="Tipe Tanda Tangan", font="Helvetica 14 bold", padx=10, pady=10)
frame3.pack(padx=30, pady=30)

r = IntVar()

Radiobutton(frame3, text="Tanda tangan dalam file         ", variable=r, value=1).pack()
Radiobutton(frame3, text="Tanda tangan secara terpisah", variable=r, value=2).pack()

button3 = Button(window, text="Tanda Tangan", padx=40, command=myClick)
button3.pack()


window.mainloop()
