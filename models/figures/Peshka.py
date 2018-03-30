from settings import *
from models.figures.AbstractFigure import AbstractFigure

class Peshka(AbstractFigure):
    crossed = False

    def __init__(self, color):
        super(Peshka, self).__init__( color)
        self.color = color
        if self.color == WHITE:
            self.id = 'p'
            self.image = 'white_peshka.png'
            self.name = 'peshka'
        if self.color == BLACK:
            self.id = 'P'
            self.image = 'black_peshka.png'
            self.name = 'peshka'


    def getAvaliableMoves(self, point, field):
        moves = []
        if self.color == WHITE:
            if not isinstance(field[point['x']][point['y'] + 1],AbstractFigure):
                moves.append({'x':point['x'], 'y':point['y'] + 1}) # simple move
            if point['y'] == 1:
                moves.append({'x':point['x'], 'y':point['y'] + 2}) # 2 cells move
            if self.avaliableFight(field, BLACK, point['x'] + 1, point['y'] + 1 ):
                moves.append({'x': point['x'] + 1, 'y': point['y'] + 1}) # fight right
            if self.avaliableFight(field, BLACK, point['x'] - 1, point['y'] + 1 ):
                moves.append({'x': point['x'] - 1, 'y': point['y'] + 1}) # fight left
            return moves
        if self.color == BLACK:
            if not isinstance(field[point['x']][point['y'] - 1], AbstractFigure):
                moves.append({'x': point['x'], 'y': point['y'] - 1})  # simple move
            if point['y'] == 6:
                moves.append({'x':point['x'], 'y':point['y'] - 2}) # 2 cells move
            if self.avaliableFight(field, WHITE, point['x'] + 1, point['y'] - 1 ):
                moves.append({'x': point['x'] + 1, 'y': point['y'] - 1}) # fight right
            if self.avaliableFight(field, WHITE, point['x'] - 1, point['y'] - 1 ):
                moves.append({'x': point['x'] - 1, 'y': point['y'] - 1}) # fight left
            return moves
        return []

    def avaliableFight(self, field, color, x, y):
        return ( self.inRange(x) and
                 self.inRange(y) and
                 isinstance(field[x][y],AbstractFigure) and field[x][y].color == color)
