from settings import *
from models.figures import AbstractFigure

class King(AbstractFigure):
    def __init__(self, color):
        super(King, self).__init__(color)
        self.color = color
        if self.color == WHITE:
            self.id = 'k'
            self.image = 'white_king.png'
            self.name = 'king'
        if self.color == BLACK:
            self.id = 'K'
            self.image = 'black_king.png'
            self.name = 'king'


    def getAvaliableMoves(self, point, field):
        return []