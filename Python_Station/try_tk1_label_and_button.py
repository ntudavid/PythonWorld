import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

s1 = tk.StringVar()
s1.set('Hello, World.')
l = tk.Label(window, textvariable=s1, bg='yellow',
             font=('Arial',16),width=16, height=4)
l.pack()

click = False
def func():
    global click
    if(click==False):
        s1.set('Hello, David.')
        click = True
    else: # if(click==True)
        s1.set('Hello, World.')
        click = False
    
b = tk.Button(window, text='David', width= 10, height=2,command=func)
b.pack()

window.mainloop()
