import tkinter as tk
import pickle

window = tk.Tk()
window.title('Log in page')
window.geometry('850x480')
# canvas
canvas = tk.Canvas(window,width=800,height=300)
im_file = tk.PhotoImage(file='leNet.png')
image = canvas.create_image(0,0, anchor='nw', image= im_file)
canvas.pack(side='top')
# label
tk.Label(window, text='User name:', font=18).place(x=250,y=330)
tk.Label(window, text='Password:', font=18).place(x=250,y=380)
# entry
user_name = tk.StringVar()
user_name.set('username@gmail.com')
tk.Entry(window,textvariable=user_name).place(x=370,y=335)
pass_word = tk.StringVar()
tk.Entry(window,textvariable=pass_word,show='*').place(x=370,y=385)
# command function
def login():
    user = user_name.get()
    pw = pass_word.get()
    try:
        file = open('users_info.pickle','rb')
        users_info = pickle.load(file)
    except FileNotFoundError:
        file = open('users_info.pickle','wb')
        users_info = {'admin':'password'}
        pickle.dump(users_info, file)
    file.close()

    if(user in users_info):
        if(pw==users_info[user]):
            tk.messagebox.showinfo(title='Log in successfully', message='Hello, '+user)
        else:
            tk.messagebox.showerror(title='Wrong password', message='Do you forget your password?')
    else:
        sign_up = tk.messagebox.askyesno(title='Sign up?', message='Do you want to sign up now?')
        if(sign_up):
            signup()
        
def signup():
    # get users_info
    try:
        file = open('users_info.pickle','rb')
        users_info = pickle.load(file)
    except FileNotFoundError:
        file = open('users_info.pickle','wb')
        users_info = {'admin':'password'}
        pickle.dump(users_info, file)
    file.close()
    
    window2 = tk.Toplevel(window)
    window2.geometry('500x280')
    window2.title('Sign Up window')
    # label
    tk.Label(window2, text='User name to sign up:', font=18).place(x=30,y=30)
    tk.Label(window2, text='Set up Password:', font=18).place(x=30,y=100)
    tk.Label(window2, text='Confirm Password:', font=18).place(x=30,y=170)
    # entry
    user_name = tk.StringVar()
    user_name.set('username@gmail.com')
    tk.Entry(window2,textvariable=user_name).place(x=250,y=35)
    pass_word = tk.StringVar()
    tk.Entry(window2,textvariable=pass_word,show='*').place(x=250,y=105)
    pass_word2 = tk.StringVar()
    tk.Entry(window2,textvariable=pass_word2,show='*').place(x=250,y=175)
    # command function
    def send():
        user = user_name.get()
        pw = pass_word.get()
        pw2 = pass_word2.get()
        if(user in users_info):
            tk.messagebox.showerror(title='Already taken', message='Try another user name.')
            window2.destroy()
            signup()
        elif(pw!=pw2):
            tk.messagebox.showerror(title='Passwords did not match', message='Retype password.')
            window2.destroy()
            signup()
        else: # sign up successfully
            tk.messagebox.showinfo(title='Sign up successfully', message='Hello, '+user)
            users_info[user] = pw
            file = open('users_info.pickle','wb')
            pickle.dump(users_info, file)
            file.close()
        window2.destroy()
            
    # button
    tk.Button(window2, text='Send', command=send).place(x=290,y=220)


# button
b1 = tk.Button(window, text='Log In', command=login)
b1.place(x=300,y=430)
b2 = tk.Button(window, text='Sign Up', command=signup)
b2.place(x=400,y=430)
