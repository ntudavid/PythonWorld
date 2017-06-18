import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x250')  # width x height

# pack
#tk.Button(window, text='pack top').pack(side='top')
#tk.Button(window, text='pack bottom').pack(side='bottom')
#tk.Button(window, text='pack left').pack(side='left')
#tk.Button(window, text='pack right').pack(side='right')

# grid
for i in range(5):
    for j in range(5):
        tk.Label(window,text=str(i)+','+str(j)).grid(row=i,column=j,padx=5,pady=5)

# place
tk.Label(window, text='@ here').place(x=200,y=100,anchor='nw')

window.mainloop()
