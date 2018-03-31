from settings import *
from tkinter import PhotoImage
from models.figures import *

class Field:
    field = None

    @staticmethod
    def getImage(AbstractFigure):
        return PhotoImage(file = IMAGE_PATH + AbstractFigure.image)


    def drawField(self, field, tk, canvas):
        figures = []

        for i in range(0, 8):
            for j in range(0, 8):
                if ((j + i) % 2 == 0):
                    color = 'white'
                else:
                    color = 'saddle brown'
                canvas.create_rectangle(START_X + i * CELL_SIZE, START_Y + j * CELL_SIZE + CELL_SIZE,
                                        START_X + i * CELL_SIZE + CELL_SIZE, START_Y + j * CELL_SIZE, fill=color)
                if isinstance(field[i][j], AbstractFigure):
                    image = Field.getImage(field[i][j])
                    figures.append(image)
                    canvas.create_image(START_X + i * CELL_SIZE + CELL_SIZE / 2,
                                        START_Y + j * CELL_SIZE + CELL_SIZE / 2, image = image)
        tk.mainloop()

    def newGame(self):
        field = [
            [None for j in range(8)]
            for i in range(8)
        ]
       
        field[0][0] = Ladya(WHITE)
        field[1][0] = Horse(WHITE)
        field[2][0] = Bishop(WHITE)
        field[3][0] = King(WHITE)
        field[4][0] = Queen(WHITE)
        field[5][0] = Bishop(WHITE)
        field[6][0] = Horse(WHITE)
        field[7][0] = Ladya(WHITE)

        for i in range(0,8):
            field[i][1] = Peshka(WHITE)

        field[0][7] = Ladya(BLACK)
        field[1][7] = Horse(BLACK)
        field[2][7] = Bishop(BLACK)
        field[3][7] = Queen(BLACK)
        field[4][7] = King(BLACK)
        field[5][7] = Bishop(BLACK)
        field[6][7] = Horse(BLACK)
        field[7][7] = Ladya(BLACK)

        for i in range(0,8):
            field[i][6] = Peshka(BLACK)

        self.field = field