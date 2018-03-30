from models.Field import *
from tkinter import *
import tkinter
import math

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
            for avaliabe_move in tmp_figure.getAvaliableMoves(tmp_point, fieldModel.field): #check it moves
                if avaliabe_move['x'] == point['x'] and avaliabe_move['y'] == point['y']:
                    fieldModel.field[point['x']][point['y']] = tmp_figure  #if we found avaliable move, go there!
                    fieldModel.field[tmp_point['x']][tmp_point['y']] = None #clear previous position
                    tmp_figure = tmp_point = None #we have no active figure
                    Field.drawField(fieldModel, fieldModel.field, tk, canvas)

        else: # we have no active figure
            if isinstance(fieldModel.field[point['x']][point['y']], AbstractFigure): # if we click on figure
                tmp_figure = fieldModel.field[point['x']][point['y']] # remember it and make it active
                tmp_point = {'x': point['x'], 'y': point['y']}
                print(tmp_figure.getAvaliableMoves(tmp_point, fieldModel.field))
                print(tmp_point)
            else: # we click on cell
                print('its empty cell')

tk = tkinter.Tk()
tk.title("Chess")
tk.bind("<Button-1>", click_field)

canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.pack(expand = YES, fill = BOTH)

fieldModel = Field()
Field.newGame(fieldModel)
Field.drawField(fieldModel,fieldModel.field, tk, canvas)








