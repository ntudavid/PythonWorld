import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

e = tk.Entry(window) # show = '*' for passwords
e.pack()

def add():
    s = e.get()
    t.insert(1.0, s) # row.offset

def insert():
    s = e.get()
    t.insert('insert', s)

def append():
    s = e.get()
    t.insert('end', s)

b1 = tk.Button(window, text='add', width= 10, height=2,command=add)
b1.pack()

b2 = tk.Button(window, text='insert', width= 10, height=2,command=insert)
b2.pack()

b3 = tk.Button(window, text='append', width= 10, height=2,command=append)
b3.pack()

t = tk.Text(window, bg='yellow', height=5)
t.pack()

window.mainloop()
