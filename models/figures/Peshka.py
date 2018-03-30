from settings import *
from models.figures.AbstractFigure import AbstractFigure

class Peshka(AbstractFigure):
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
        if self.id == 'p': # white peshka rules
            moves = [{'x':point['x'], 'y':point['y'] + 1}]
            if point['y'] == 1:
                moves.append({'x':point['x'], 'y':point['y'] + 2})
            if isinstance(field[point['x'] + 1][point['y'] + 1],AbstractFigure) and field[point['x'] + 1][point['y'] + 1].color == BLACK:
                moves.append({'x': point['x'] + 1, 'y': point['y'] + 1})
            if isinstance(field[point['x'] - 1][point['y'] + 1], AbstractFigure) and field[point['x'] - 1][ point['y'] + 1].color == BLACK:
                moves.append({'x': point['x'] - 1, 'y': point['y'] + 1})
            return moves
        if self.id == 'P':# black peshka rules
            moves = [{'x':point['x'], 'y':point['y'] - 1}]
            if point['y'] == 6:
                moves.append({'x':point['x'], 'y':point['y'] - 2})
            if isinstance(field[point['x'] + 1][point['y'] - 1], AbstractFigure) and field[point['x'] + 1][point['y'] - 1].color == WHITE:
                moves.append({'x': point['x'] + 1, 'y': point['y'] - 1})
            if isinstance(field[point['x'] - 1][point['y'] - 1], AbstractFigure) and field[point['x'] - 1][point['y'] - 1].color == WHITE:
                moves.append({'x': point['x'] - 1, 'y': point['y'] - 1})
            return moves
        return []