from models.Field import *
from tkinter import *
import tkinter
import math

tmp_figure = None
tmp_point = None
def getCell(x, y):
    return {'x': math.floor((x - START_X)/CELL_SIZE), 'y': math.floor((y - START_Y)/CELL_SIZE)}

white_to_move = True
def click_field(event):
    global tmp_figure
    global tmp_point
    global white_to_move
    point = getCell(event.x, event.y)
    if 0 <= point['x'] <= 7 and 0 <= point['y'] <= 7:
        if(tmp_figure != None and tmp_point != None): #we have active figure
            for avaliabe_move in tmp_figure.getAvaliableMoves(tmp_point, fieldModel.field): #check it moves
                if avaliabe_move['x'] == point['x'] and avaliabe_move['y'] == point['y']:
                    #make move
                    if isinstance(tmp_figure, Peshka) and tmp_figure.crossed: #if we move already crossed peshka ->its not crossed any more
                        tmp_figure.crossed = False
                    else:
                        if 'crossed' in avaliabe_move:
                            if avaliabe_move['crossed']: #if we move on 2 ways on peshka, then its marked as crossed
                                tmp_figure.crossed = True
                            else:
                                tmp_figure.crossed = False
                    fieldModel.field[point['x']][point['y']] = tmp_figure  #if we found avaliable move, go there!
                    fieldModel.field[tmp_point['x']][tmp_point['y']] = None #clear previous position

                    # del crossed figure
                    if 'cross' in avaliabe_move:
                        if avaliabe_move['cross'] == True :
                            if fieldModel.field[point['x']][point['y']].color == BLACK:
                                fieldModel.field[avaliabe_move['x']][avaliabe_move['y'] + 1] = None
                            else:
                                fieldModel.field[avaliabe_move['x']][avaliabe_move['y'] - 1] = None

                    tmp_figure = tmp_point = None #we have no active figure
                    white_to_move = not white_to_move #switch moves

                    #check if king under attack 'check'?TODO
                    # ни одна фигура данного цвета не может пойти куда-то, если при следующем ходе будет убит король.
                    # оставляем ходы которые сделают так, что бы короля не можно было убить следующим ходом

                    #transform peshka when got 8th line TODO

                    Field.drawField(fieldModel, fieldModel.field, tk, canvas)
                else: #if we click on wrong field
                    if (isinstance(fieldModel.field[point['x']][point['y']], AbstractFigure) and #its figure
                            fieldModel.field[point['x']][point['y']].color == white_to_move): #its friend figure
                        makeActive(point)
        else: # we have no active figure
            if isinstance(fieldModel.field[point['x']][point['y']], AbstractFigure) and fieldModel.field[point['x']][point['y']].color == white_to_move: # if we click on figure
                makeActive(point)
            else: # we click on cell
                print('its empty cell, or its not your move!')


def makeActive(point):
    global tmp_figure
    global tmp_point
    tmp_figure = fieldModel.field[point['x']][point['y']]  # remember it and make it active
    tmp_point = {'x': point['x'], 'y': point['y']}
    print('aval moves:')
    print(tmp_figure.getAvaliableMoves(tmp_point, fieldModel.field))
    print(tmp_point)


tk = tkinter.Tk()
tk.title("Chess")
tk.bind("<Button-1>", click_field)

canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.pack(expand = YES, fill = BOTH)

fieldModel = Field()
Field.newGame(fieldModel)
Field.drawField(fieldModel,fieldModel.field, tk, canvas)








