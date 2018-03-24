from models.Field import *

import math as math

tmp_figure = None
tmp_point = None

def getCell(x, y):
    return {'x': math.floor((x - START_X)/CELL_SIZE), 'y': math.floor((y - START_Y)/CELL_SIZE)}


def click_field(event):
    global tmp_figure
    global tmp_point
    point = getCell(event.x, event.y)
    if 0 <= point['x'] < 8 and 0 <= point['y'] < 8:
        if(tmp_figure != None and tmp_point != None): #we have active figure
            for avaliabe_move in tmp_figure.getAvaliableMoves(tmp_point, FIELD): #check it moves
                if avaliabe_move['x'] == point['x'] and avaliabe_move['y'] == point['y']:
                    FIELD[point['x']][point['y']] = tmp_figure  #if we found avaliable move, go there!
                    FIELD[tmp_point['x']][tmp_point['y']] = None #clear previous position
                    tmp_figure = tmp_point = None #we have no active figure
                    Field.drawField(FIELD)
        else: # we have no active figure
            if (isinstance(FIELD[point['x']][point['y']], Figure)): # if we click on figure
                tmp_figure = FIELD[point['x']][point['y']] # remember it and make it active
                tmp_point = {'x': point['x'], 'y': point['y']}
                print(tmp_figure.getAvaliableMoves(tmp_point, FIELD))
                print(tmp_point)
            else: # we click on cell
                print('its empty cell')


tk.bind("<Button-1>", click_field)
