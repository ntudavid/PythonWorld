import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

s1 = tk.StringVar()
s1.set('SetVolume')
l = tk.Label(window, textvariable=s1, bg='yellow', width=15)
l.pack()

def print_selection(v):
    s1.set(v)

s = tk.Scale(window, label='volume', from_=0, to=10, orient=tk.HORIZONTAL,
             length=300, showvalue=1, tickinterval=2, resolution=0.5,
             command=print_selection)
s.pack()

window.mainloop()
