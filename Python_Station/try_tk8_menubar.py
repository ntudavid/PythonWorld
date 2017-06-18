import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x250')  # width x height

l = tk.Label(window,text='',bg='yellow')
l.pack()

cnt1 = 0
cnt2 = 0
def print_select1():
    global cnt1
    cnt1 += 1
    l.config(text='config x '+str(cnt1))

def print_select2():
    global cnt2
    cnt2 += 1
    l.config(text='import x '+str(cnt2))

menubar = tk.Menu(window)

options_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Options', menu=options_menu)
options_menu.add_command(label='Configure IDLE', command=print_select1)
options_menu.add_command(label='Code Context', command=print_select1)

submenu = tk.Menu(options_menu)
options_menu.add_cascade(label='import from', menu=submenu, underline=0)
submenu.add_command(label='source1', command=print_select2)
submenu.add_command(label='source2', command=print_select2)
    
options_menu.add_separator()
options_menu.add_command(label='Quit')

run_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Run', menu=run_menu)
run_menu.add_command(label='Check Module', command=print_select1)
run_menu.add_separator()
run_menu.add_command(label='Run Module', command=print_select1)

window.config(menu=menubar)
window.mainloop()
