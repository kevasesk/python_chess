class AbstractFigure:
    image = ''

    TOP     = 0
    RIGHT   = 1
    BOTTOM  = 2
    LEFT    = 3

    TOP_LEFT     = 4
    TOP_RIGHT    = 5
    BOTTOM_LEFT  = 6
    BOTTOM_RIGHT = 7

    def __init__(self, color):
        self.color = color

    def getAvaliableMoves(self, point, field):
        return []
    @staticmethod
    def inRange(coordinate):
        return 0 <= coordinate <= 7

    def checkMove(self, field,  x, y):
        return (self.inRange(x) and # new position in range 0 <> 7
                self.inRange(y) and # new position in range 0 <> 7
                (not isinstance(field[x][y], AbstractFigure) or # new place is empty
                not field[x][y].color == self.color )) # new place is enemy figure

    def line(self, point, field, type):
        moves = []
        psevdoX = point['x']
        psevdoY = point['y']
        for i in range(0, 8):

            if(type == self.TOP_LEFT):
                psevdoX = psevdoX - 1
                psevdoY = psevdoY - 1
            if (type == self.TOP_RIGHT):
                psevdoX = psevdoX + 1
                psevdoY = psevdoY - 1
            if (type == self.BOTTOM_LEFT):
                psevdoX = psevdoX - 1
                psevdoY = psevdoY + 1
            if (type == self.BOTTOM_RIGHT):
                psevdoX = psevdoX + 1
                psevdoY = psevdoY + 1

            if (type == self.TOP):
                psevdoY = psevdoY - 1
            if (type == self.RIGHT):
                psevdoX = psevdoX + 1
            if (type == self.BOTTOM):
                psevdoY = psevdoY + 1
            if (type == self.LEFT):
                psevdoX = psevdoX - 1

            if self.inRange(psevdoX) and self.inRange(psevdoY):
                if isinstance(field[psevdoX][psevdoY], AbstractFigure): # we saw figure
                    if not field[psevdoX][psevdoY].color == self.color: #is it enemy?
                        moves.append({'x': psevdoX, 'y': psevdoY}) # we can go there and stop cycle dyagonal
                        break
                    else:  # its our figure
                        break
                else:
                    moves.append({'x': psevdoX, 'y': psevdoY})
        return moves