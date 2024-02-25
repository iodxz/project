import pygame as pg
import math

l = 30
sc = pg.display.set_mode((801, 801))
color_line = (255, 255, 255)
color_main_line = (255, 255, 0)
line_width = 7
line_main_width = 10
count_cross = 0
count_circle = 0
BLACK = (0,0,0)
ceil_x = 0
ceil_x = 0
#field = [[[['_' for t in range(3)] for j in range(3)] for k in range(3)] for p in range(3)]
field = [[[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]],

     [[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]],

     [[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']],
      [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]]]

for verticals in range(89, 801, 89):
    pg.draw.line(sc, color_line, (verticals, 0), (verticals, 801), line_width)
    if verticals%267 == 0:
        pg.draw.line(sc, color_main_line, (verticals, 0), (verticals, 801), line_main_width)



for horizontals in range(89, 801, 89):
    pg.draw.line(sc, color_line, (0, horizontals), (801, horizontals), line_width)
    if horizontals%267 == 0:
        pg.draw.line(sc, color_main_line, (0, horizontals), (801, horizontals), line_main_width)
pg.display.update()

def circle(x_m,y_m):
    global ceil_x
    global ceil_y
    pg.draw.circle(sc, color_line, (x * 89 + 44.5, y * 89 + 44.5), 30)
    pg.draw.circle(sc, BLACK, (x * 89 + 44.5, y * 89 + 44.5), 20)
    global count_circle
    count_circle+=1
    ceil_x = (x + 1 - x0) - 1
    ceil_y = (y + 1 - y0) - 1
    field[x_main][y_main][ceil_x][ceil_y] = 0


    pg.display.update()


def cross(x_m,y_m,x_main,y_main,x0, y0):

    global count_cross

    pg.draw.line(sc, color_line, (44.5 + (x) * 89 - l, 44.5 + (y) * 89 - l),
                 (44.5 + (x) * 89 + l, 44.5 + (y) * 89 + l), 20)
    pg.draw.line(sc, color_line, (44.5 + (x) * 89 - l, 44.5 + (y) * 89 + l),
                 (44.5 + (x) * 89 + l, 44.5 + (y) * 89 - l), 20)

    global ceil_x
    global ceil_y
    ceil_x = (x + 1 - x0) - 1
    ceil_y = (y + 1 - y0) - 1
    field[x_main][y_main][ceil_x][ceil_y] = 1
    count_cross+=1
    pg.display.update()

def check(x_m,y_m,x_main,y_main, x0, y0):

    if ceil_x == x_main and ceil_y == y_main:

        if count_cross == count_circle:
            cross(x_m,y_m,x_main,y_main,x0, y0)
        elif count_cross > count_circle:
            circle(x_m,y_m)


end = True
while end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = False
            pg.quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            x_m, y_m = pg.mouse.get_pos()
            x_main = math.ceil(x_m / (801/ 3)) - 1
            y_main = math.ceil(y_m / (801 / 3)) - 1
            x = math.ceil(x_m / (801/ 9)) - 1
            y = math.ceil(y_m / (801 / 9)) - 1

            x0 = x_main * 3
            y0 = y_main * 3

            if count_cross == 0 and count_circle == 0:

                ceil_x = (x + 1 - x0) - 1
                ceil_y = (y + 1 - y0) - 1
                pg.draw.line(sc, color_line, (44.5 + (x) * 89 - l, 44.5 + (y) * 89 - l),
                             (44.5 + (x) * 89 + l, 44.5 + (y) * 89 + l), 20)
                pg.draw.line(sc, color_line, (44.5 + (x) * 89 - l, 44.5 + (y) * 89 + l),
                             (44.5 + (x) * 89 + l, 44.5 + (y) * 89 - l), 20)
                count_cross += 1

                pg.display.update()

            else:

                print('main =', x_main, y_main, 'ceil =', ceil_x, ceil_y, 'count', count_cross, count_circle)
                check(x_m,y_m,x_main,y_main, x0, y0)

