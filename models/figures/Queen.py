from settings import *
from models.figures import AbstractFigure

class Queen(AbstractFigure):
    def __init__(self, color):
        super(Queen, self).__init__(color)
        self.color = color
        if self.color == WHITE:
            self.id = 'q'
            self.image = 'white_queen.png'
            self.name = 'queen'
        if self.color == BLACK:
            self.id = 'Q'
            self.image = 'black_queen.png'
            self.name = 'queen'


    def getAvaliableMoves(self, point, field):
        return []