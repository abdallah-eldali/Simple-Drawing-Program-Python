from tkinter import *
from math import *

tk = Tk()
canvas = Canvas(tk, cursor="plus")

def drawLine(event):
    x, y = event.x, event.y

    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y

tk.bind('<Motion>', drawLine)
canvas.pack()
canvas.old_coords = None

tk.mainloop()