from tkinter import *

path = "./images/figures/"
class Figure:
    def __init__(self, name, color, id, image):
        self.name = name
        self.color = color
        self.id = id
        self.image = image
    def getImage(self):
        return PhotoImage(file = path + self.image)



white_peshka = Figure('peshka', 'white','p', 'white_peshka.png')
white_ladya  = Figure('ladya',  'white','t', 'white_ladya.png')
white_horse  = Figure('horse',  'white','h', 'white_horse.png')
white_bishop = Figure('bishop', 'white','b', 'white_bishop.png')
white_queen  = Figure('queen',  'white','q', 'white_queen.png')
white_king   = Figure('king',   'white','k', 'white_king.png')

black_peshka = Figure('peshka', 'black','P', [250, 50, 300, 200])
black_ladya  = Figure('ladya',  'black','T', [200, 50, 250, 150])
black_horse  = Figure('horse',  'black','H', [150, 50, 200, 150])
black_bishop = Figure('bishop', 'black','B', [100, 50, 150, 150])
black_queen  = Figure('queen',  'black','Q', [50, 50, 100, 150])
black_king   = Figure('king',   'black','K', [0, 50, 50, 150])

