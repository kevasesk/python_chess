from settings import *
from models.figures import AbstractFigure

class Horse(AbstractFigure):
    def __init__(self, color):
        super(Horse, self).__init__(color)
        self.color = color
        if self.color == WHITE:
            self.id = 'h'
            self.image = 'white_horse.png'
            self.name = 'horse'
        if self.color == BLACK:
            self.id = 'H'
            self.image = 'black_horse.png'
            self.name = 'horse'

    def getAvaliableMoves(self, point, field):
        moves = []

        if self.checkMove(field, point['x'] - 1, point['y'] - 2):
            moves.append({'x': point['x'] - 1, 'y': point['y'] - 2})
        if self.checkMove(field, point['x'] + 1, point['y'] - 2):
            moves.append({'x': point['x'] + 1, 'y': point['y'] - 2})

        if self.checkMove(field, point['x'] - 2, point['y'] - 1):
            moves.append({'x': point['x'] - 2, 'y': point['y'] - 1})
        if self.checkMove(field, point['x'] + 2, point['y'] - 1):
            moves.append({'x': point['x'] + 2, 'y': point['y'] - 1})

        if self.checkMove(field, point['x'] - 2, point['y'] + 1):
            moves.append({'x': point['x'] - 2, 'y': point['y'] + 1})
        if self.checkMove(field, point['x'] + 2, point['y'] + 1):
            moves.append({'x': point['x'] + 2, 'y': point['y'] + 1})

        if self.checkMove(field, point['x'] - 1, point['y'] + 2):
            moves.append({'x': point['x'] - 1, 'y': point['y'] + 2})
        if self.checkMove(field, point['x'] + 1, point['y'] + 2):
            moves.append({'x': point['x'] + 1, 'y': point['y'] + 2})

        return moves
