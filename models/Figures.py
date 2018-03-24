from settings import *
from tkinter import PhotoImage

WHITE = True
BLACK = False
class Figure:
    def __init__(self, name, color, id, image):
        self.name = name
        self.color = color
        self.id = id
        self.image = image
    def getImage(self):
        return PhotoImage(file = IMAGE_PATH + self.image)

    def getAvaliableMoves(self, point, field):
        if self.id == 'p': # white peshka rules
            moves = [{'x':point['x'], 'y':point['y'] + 1}]
            if point['y'] == 1:
                moves.append({'x':point['x'], 'y':point['y'] + 2})
            if isinstance(field[point['x'] + 1][point['y'] + 1],Figure) and field[point['x'] + 1][point['y'] + 1].color == BLACK:
                moves.append({'x': point['x'] + 1, 'y': point['y'] + 1})
            if isinstance(field[point['x'] - 1][point['y'] + 1], Figure) and field[point['x'] - 1][ point['y'] + 1].color == BLACK:
                moves.append({'x': point['x'] - 1, 'y': point['y'] + 1})
            return moves
        if self.id == 'P':# black peshka rules
            moves = [{'x':point['x'], 'y':point['y'] - 1}]
            if point['y'] == 6:
                moves.append({'x':point['x'], 'y':point['y'] - 2})
            if isinstance(field[point['x'] + 1][point['y'] - 1], Figure) and field[point['x'] + 1][point['y'] - 1].color == WHITE:
                moves.append({'x': point['x'] + 1, 'y': point['y'] - 1})
            if isinstance(field[point['x'] - 1][point['y'] - 1], Figure) and field[point['x'] - 1][point['y'] - 1].color == WHITE:
                moves.append({'x': point['x'] - 1, 'y': point['y'] - 1})
            return moves
        return []

class Figures:
    white_peshka = Figure('white_peshka', WHITE,'p', 'white_peshka.png')
    white_ladya  = Figure('white_ladya',  WHITE,'t', 'white_ladya.png')
    white_horse  = Figure('white_horse',  WHITE,'h', 'white_horse.png')
    white_bishop = Figure('white_bishop', WHITE,'b', 'white_bishop.png')
    white_queen  = Figure('white_queen',  WHITE,'q', 'white_queen.png')
    white_king   = Figure('white_king',   WHITE,'k', 'white_king.png')

    black_peshka = Figure('black_peshka', BLACK,'P', 'black_peshka.png')
    black_ladya  = Figure('black_ladya',  BLACK,'T', 'black_ladya.png')
    black_horse  = Figure('black_horse',  BLACK,'H', 'black_horse.png')
    black_bishop = Figure('black_bishop', BLACK,'B', 'black_bishop.png')
    black_queen  = Figure('black_queen',  BLACK,'Q', 'black_queen.png')
    black_king   = Figure('black_king',   BLACK,'K', 'black_king.png')

