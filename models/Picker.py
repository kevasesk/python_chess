from settings import *
from models.figures import *
from models.Field import Field


class Picker:

    canvas = None

    def __init__(self, canvas):
        self.canvas = canvas

    def drawSelecterBackground(self):
        self.canvas.create_rectangle(BACKGROUND_X1, BACKGROUND_Y1, BACKGROUND_X2, BACKGROUND_Y2, fill=BACKGROUND_COLOR)

    def drawPeshkaOptions(self, color):
        images = []
        figuresToChoise = [
            Ladya,
            Horse,
            Bishop,
            Queen
        ]
        for Figure in figuresToChoise :
            pointX = pointY = None
            if Figure == Ladya :
                pointX = pointY = 3
            elif Figure == Horse :
                pointX = 3
                pointY = 4
            elif Figure == Bishop:
                pointX = 4
                pointY = 3
            elif Figure == Queen:
                pointX = pointY = 4

            image = Field.getImage(Figure(color))
            self.canvas.create_image((Picker.getCell(pointX), Picker.getCell(pointY)), image = image)
            images.append(image)
        return images

    @staticmethod
    def getCell(number):
        return START_X + number * CELL_SIZE + CELL_SIZE / 2