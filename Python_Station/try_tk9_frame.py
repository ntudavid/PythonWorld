import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x250')  # width x height

tk.Label(window,text='window',bg='yellow').pack()

f = tk.Frame(window)
f.pack()
f1 = tk.Frame(f)
f1.pack(side='left')
tk.Label(f1,text='frame left1',bg='red').pack()
tk.Label(f1,text='frame left2',bg='red').pack()
f2 = tk.Frame(f)
f2.pack(side='right')
tk.Label(f2,text='frame right1',bg='blue').pack()

window.mainloop()
