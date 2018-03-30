class AbstractFigure:
    image = ''

    def __init__(self, color):
        self.color = color

    def getAvaliableMoves(self, point, field):
        return []