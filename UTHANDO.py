from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    L2 = Label(top, text="this is toplevel window")
    L2.pack()

    top.mainloop()

L = Label(root, text="this is root window")
btn = Button(root, text="open toplevel window", command=topwin)

L.pack()
btn.pack()

root.mainloop()