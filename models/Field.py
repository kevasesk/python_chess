from models.Figures import Figures
from models.Figures import Figure
from settings import *
from tkinter import *


import tkinter

tk = tkinter.Tk()
tk.title("Chess")

canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.pack(expand = YES, fill = BOTH)

class Field:
    def drawField(field):
        figures = []

        for i in range(0, 8):
            for j in range(0, 8):
                if ((j + i) % 2 == 0):
                    color = 'white'
                else:
                    color = 'saddle brown'
                canvas.create_rectangle(START_X + i * CELL_SIZE, START_Y + j * CELL_SIZE + CELL_SIZE,
                                        START_X + i * CELL_SIZE + CELL_SIZE, START_Y + j * CELL_SIZE, fill=color)
                if (isinstance(field[i][j], Figure)):
                    image = Figure.getImage(field[i][j])
                    figures.append(image)
                    canvas.create_image(START_X + i * CELL_SIZE + CELL_SIZE / 2,
                                        START_Y + j * CELL_SIZE + CELL_SIZE / 2, image=image)
        mainloop()
    def newGame():
        field = [
            [None for j in range(8)]
            for i in range(8)
        ]

        field[0][0] = Figures.white_ladya
        field[1][0] = Figures.white_horse
        field[2][0] = Figures.white_bishop
        field[3][0] = Figures.white_king
        field[4][0] = Figures.white_queen
        field[5][0] = Figures.white_bishop
        field[6][0] = Figures.white_horse
        field[7][0] = Figures.white_ladya

        field[0][1] = Figures.white_peshka
        field[1][1] = Figures.white_peshka
        field[2][1] = Figures.white_peshka
        field[3][1] = Figures.white_peshka
        field[4][1] = Figures.white_peshka
        field[5][1] = Figures.white_peshka
        field[6][1] = Figures.white_peshka
        field[7][1] = Figures.white_peshka

        field[0][7] = Figures.black_ladya
        field[1][7] = Figures.black_horse
        field[2][7] = Figures.black_bishop
        field[3][7] = Figures.black_king
        field[4][7] = Figures.black_queen
        field[5][7] = Figures.black_bishop
        field[6][7] = Figures.black_horse
        field[7][7] = Figures.black_ladya

        field[0][6] = Figures.black_peshka
        field[1][6] = Figures.black_peshka
        field[2][6] = Figures.black_peshka
        field[3][6] = Figures.black_peshka
        field[4][6] = Figures.black_peshka
        field[5][6] = Figures.black_peshka
        field[6][6] = Figures.black_peshka
        field[7][6] = Figures.black_peshka

        return field


FIELD = Field.newGame()
