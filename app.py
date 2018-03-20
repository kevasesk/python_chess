from tkinter import *
from settings import *

def drawField(field):
    size = CELL_SIZE
    canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
    canvas.pack(expand = YES, fill = BOTH)
    figures = []

    for i in range(0,8):
        for j in range(0,8):
            if ((j+i)%2 == 0):
                color = 'white'
            else:
                color = 'black'
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
    drawField(field)

newGame()
