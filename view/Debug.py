from models.Field import *

import math as math

mouse_x = StringVar()
mouse_y = StringVar()

x_field = Entry(tk, textvariable = str(mouse_x))
y_field = Entry(tk, textvariable = str(mouse_y))

x_field.place(x = 800, y = 200)
y_field.place(x = 800, y = 220)
canvas.create_text(770, 210, text = 'Column:')
canvas.create_text(780, 230, text = 'Row:')

def motion(event):
    x, y = event.x, event.y
    mouse_x.set(str(math.floor((x - START_X)/CELL_SIZE)))
    mouse_y.set(str(math.floor((y - START_Y)/CELL_SIZE)))


tk.bind('<Motion>', motion)
