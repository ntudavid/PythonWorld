import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

s1 = tk.StringVar()

l = tk.Label(window, textvariable=s1, bg='yellow', width=10)
l.pack()

def select():
    sel = lb.get(lb.curselection())
    s1.set(sel)
    
b = tk.Button(window, text='select', width= 10, height=2,command=select)
b.pack()

s2 = tk.StringVar()
s2.set(('Jan','Feb','Mar','Apr','May'))
lb = tk.Listbox(window,listvariable=s2)
list_item = ['Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in list_item:
    lb.insert('end',i)
lb.pack()

window.mainloop()
