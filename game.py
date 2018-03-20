from settings import *
import math as math
import tkinter as tkinter

tk = tkinter.Tk()
tk.title("Chess")

canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack(expand=YES, fill=BOTH)

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

def drawField(field):
    size = CELL_SIZE

    figures = []

    for i in range(0,8):
        for j in range(0,8):
            if ((j+i)%2 == 0):
                color = 'white'
            else:
                color = 'saddle brown'
            canvas.create_rectangle(
                START_X + i * size,
                START_Y + j*size + size,
                START_X + i * size + size,
                START_Y + j*size,
                fill = color
            )

    for i in range(0, 8):
        for j in range(0, 8):
            if (isinstance(field[i][j],Figure)):
                image = Figure.getImage(field[i][j])
                figures.append(image)
                canvas.create_image(START_X + i * size + size/2, START_Y + j * size + size/2, image = image)
    mainloop()
def newGame():
    field = [
        [None for j in range(8)]
        for i in range(8)
    ]

    field[0][0] = white_ladya
    field[1][0] = white_horse
    field[2][0] = white_bishop
    field[3][0] = white_king
    field[4][0] = white_queen
    field[5][0] = white_bishop
    field[6][0] = white_horse
    field[7][0] = white_ladya

    field[0][1] = white_peshka
    field[1][1] = white_peshka
    field[2][1] = white_peshka
    field[3][1] = white_peshka
    field[4][1] = white_peshka
    field[5][1] = white_peshka
    field[6][1] = white_peshka
    field[7][1] = white_peshka
	
    field[0][7] = black_ladya
    field[1][7] = black_horse
    field[2][7] = black_bishop
    field[3][7] = black_king
    field[4][7] = black_queen
    field[5][7] = black_bishop
    field[6][7] = black_horse
    field[7][7] = black_ladya

    field[0][6] = black_peshka
    field[1][6] = black_peshka
    field[2][6] = black_peshka
    field[3][6] = black_peshka
    field[4][6] = black_peshka
    field[5][6] = black_peshka
    field[6][6] = black_peshka
    field[7][6] = black_peshka

    return field

field = newGame()
drawField(field)



tk.mainloop()

