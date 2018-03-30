class AbstractFigure:
    image = ''

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