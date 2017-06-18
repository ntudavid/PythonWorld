import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

s1 = tk.StringVar()
s1.set('Education level')
l = tk.Label(window, textvariable=s1, bg='yellow', width=15)
l.pack(anchor = tk.W)

var = tk.StringVar()

def select():
    l.config(bg='red')
    s1.set(var.get())
 
rb1 = tk.Radiobutton(window, text='College',
                     variable=var, value='College', command=select)
rb1.pack(anchor = tk.W)

rb2 = tk.Radiobutton(window, text='Graduate',
                     variable=var, value='Graduate', command=select)
rb2.pack(anchor = tk.W)

rb3 = tk.Radiobutton(window, text='ph.D',
                     variable=var, value='ph.D', command=select)
rb3.pack(anchor = tk.W)

window.mainloop()
