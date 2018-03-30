from settings import *
from models.figures import AbstractFigure

class Ladya(AbstractFigure):
    def __init__(self, color):
        super(Ladya, self).__init__(color)
        self.color = color
        if self.color == WHITE:
            self.id = 't'
            self.image = 'white_ladya.png'
            self.name = 'ladya'
        if self.color == BLACK:
            self.id = 'T'
            self.image = 'black_ladya.png'
            self.name = 'ladya'


    def getAvaliableMoves(self, point, field):
        return []