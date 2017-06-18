import tkinter as tk

window = tk.Tk()
window.title('test window')
window.geometry('500x700')  # width x height

canvas = tk.Canvas(window, bg='yellow', width=500, height=500)
# image
im_file =tk.PhotoImage(file='fb.png')
image = canvas.create_image(100,200, anchor='nw', image=im_file)
# drawing
x0,y0,x1,y1 = 20,30,150,250
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='blue')
arc = canvas.create_arc(x0+70,y0+50,x1,y1,start=30,extent=150)
rect = canvas.create_rectangle(200,200,200+50,200+50)
canvas.pack()

def move_rect():
    canvas.move(rect,2,5) # drawing object, move_X, move_Y

b = tk.Button(window, text='rect_move', command=move_rect).pack()

window.mainloop()
