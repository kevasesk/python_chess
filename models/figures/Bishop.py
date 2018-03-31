from settings import *
from models.figures import AbstractFigure


class Bishop(AbstractFigure):

    def __init__(self, color):
        super(Bishop, self).__init__(color)
        self.color = color
        if self.color == WHITE:
            self.id = 'b'
            self.image = 'white_bishop.png'
            self.name = 'bishop'
        if self.color == BLACK:
            self.id = 'B'
            self.image = 'black_bishop.png'
            self.name = 'bishop'


    def getAvaliableMoves(self, point, field):
        moves = []

        moves += self.line(point, field, self.TOP_LEFT)
        moves += self.line(point, field, self.TOP_RIGHT)
        moves += self.line(point, field, self.BOTTOM_LEFT)
        moves += self.line(point, field, self.BOTTOM_RIGHT)

        return moves
