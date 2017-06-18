import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x250')  # width x height

def delete():
    tk.messagebox.showinfo(title='confirm', message='It can go back after this.')
    tk.messagebox.showwarning(title='double check', message='Are you sure?')
    tk.messagebox.showerror(title='error occurs', message='CAN NOT DELETE!')
    reply = tk.messagebox.askquestion(title='confirm', message='Are you sure?') # return 'yes'/'no'
    if(reply=='yes'):
        print('Yes, go ahead')
    else:
        print('Wait, I need to think about it.')
    ans = tk.messagebox.askyesno(title='yes or no', message='Yes or No') # return True/False
    if(ans):
        print('Answer is YES.')
    else:
        print('Answer is NO.')
        
tk.Button(window, text='Delete',command=delete).pack()

window.mainloop()
