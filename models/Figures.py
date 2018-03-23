from settings import *
from tkinter import PhotoImage

class Figure:
    def __init__(self, name, color, id, image):
        self.name = name
        self.color = color
        self.id = id
        self.image = image
    def getImage(self):
        return PhotoImage(file = IMAGE_PATH + self.image)


class Figures:
    white_peshka = Figure('peshka', 'white','p', 'white_peshka.png')
    white_ladya  = Figure('ladya',  'white','t', 'white_ladya.png')
    white_horse  = Figure('horse',  'white','h', 'white_horse.png')
    white_bishop = Figure('bishop', 'white','b', 'white_bishop.png')
    white_queen  = Figure('queen',  'white','q', 'white_queen.png')
    white_king   = Figure('king',   'white','k', 'white_king.png')

    black_peshka = Figure('peshka', 'black','P', 'black_peshka.png')
    black_ladya  = Figure('ladya',  'black','T', 'black_ladya.png')
    black_horse  = Figure('horse',  'black','H', 'black_horse.png')
    black_bishop = Figure('bishop', 'black','B', 'black_bishop.png')
    black_queen  = Figure('queen',  'black','Q', 'black_queen.png')
    black_king   = Figure('king',   'black','K', 'black_king.png')

