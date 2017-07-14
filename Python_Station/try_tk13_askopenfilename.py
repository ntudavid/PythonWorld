import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x200')  # width x height

s1 = tk.StringVar()
s1.set('File Path')
l = tk.Label(window,textvariable=s1,font=('Arial',10),width=220, height=4)
l.pack()

click = False
def func():
    file_path = tk.filedialog.askopenfilename()
    s1.set(file_path)
    
b = tk.Button(window,text='File Open',font=('Arial',14),width= 16, height=2,command=func)
b.pack()

window.mainloop()
