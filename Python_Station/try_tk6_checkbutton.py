import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x300')  # width x height

s1 = tk.StringVar()
s1.set('Select Language')
l = tk.Label(window, textvariable=s1, bg='yellow', width=15)
l.pack()

def selections():
    if((var1.get()==1) and (var2.get()==1)):
        s1.set('You are bilingual!')
    elif(var1.get()==1):
        s1.set('English Speaker')
    elif(var2.get()==1):
        s1.set('Mandrin Speaker')
    else:
        s1.set('Can you speak?')

var1 = tk.IntVar()
cb1 = tk.Checkbutton(window, text='English', variable=var1,
                     onvalue=1, offvalue=0, command=selections)
cb1.pack()

var2 = tk.IntVar()
cb2 = tk.Checkbutton(window, text='Mandrin', variable=var2,
                     onvalue=1, offvalue=0, command=selections)
cb2.pack()

window.mainloop()
