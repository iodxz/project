import pygame as pg
import math

sc = pg.display.set_mode((900, 900))
stop = True
circle = []
cross = []
pole = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
sc.fill((255, 255,  255))
l = 100

#def print_pole(pole):
#    for y in pole:
#        for x in y:
#            if x == 0:
#                print("_", end="")
#            if x == 1:
#                print("0", end="")
#            if x == 2:
#                print("x", end="")
#        print("\n")
def draw(x, y):
    x1 = math.ceil(x / (900 / 3)) -1
    y1 = math.ceil(y / (900 / 3)) -1

    if win == False:
        if len(cross) > len(circle):
            if pole[y1][x1] == 0:
                pg.draw.circle(sc, (0, 0, 0), (150 + (x1) * 300, 150 + (y1) * 300), 148)
                pg.draw.circle(sc, (255, 255, 255), (150 + (x1) * 300, 150 + (y1) * 300), 130)
                circle.append(1)
                pole[y1][x1] = 1
        else:
            if pole[y1][x1] == 0:
                pole[y1][x1] = 2
                pg.draw.line(sc, (0, 0, 0), (150+(x1) * 300 - l, 150+(y1) * 300- l), (150+(x1) * 300 + l, 150+(y1) * 300 + l), 20)
                pg.draw.line(sc, (0, 0, 0), (150 + (x1) * 300 - l, 150 + (y1) * 300 + l),(150 + (x1) * 300 + l, 150 + (y1) * 300 - l), 20)
                cross.append(2)
win = False
while stop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop = False
            break

        pg.draw.line(sc, (0, 0, 0), (300, 0), (300, 900), 2)
        pg.draw.line(sc, (0, 0, 0), (600, 0), (600, 900), 2)
        pg.draw.line(sc, (0, 0, 0), (0, 300), (900, 300), 2)
        pg.draw.line(sc, (0, 0, 0), (0, 600), (900, 600), 2)
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            draw(x,y)
        finish = 0


        if pole[0][0] == pole[1][1] == pole [2][2] == 1 or pole[0][0] == pole[1][1] == pole [2][2] == 2:
            win = True
            pg.draw.line(sc, (255, 0, 0), (100, 100), (750, 750), 5)
        if pole[2][0] == pole[1][1] == pole[0][2] != 0:
            win = True
            pg.draw.line(sc, (255, 0, 0), (100, 800), (800, 100), 50)
        for end in range(3):
            if pole[end] == [1, 1, 1] or pole[end] == [2, 2, 2]:
                win = True
                if end == 0:
                    pg.draw.line(sc, (255, 0, 0), (0, 150), (900, 150), 50)
                elif end == 1:
                    pg.draw.line(sc, (255, 0, 0), (0, 450), (900, 450), 50)
                else:
                    pg.draw.line(sc, (255, 0, 0), (0, 750), (900, 750), 50)
        for end_v in range(3):
            if pole[0][end_v] ==  pole[1][end_v] ==  pole[2][end_v] == 1 or pole[0][end_v] ==  pole[1][end_v] ==  pole[2][end_v] == 2:
                win = True
                if end_v == 0:
                    pg.draw.line(sc, (255, 0, 0), (150, 100),(150, 800) , 50)
                if end_v == 1:
                    pg.draw.line(sc, (255, 0, 0), (450, 100),(450, 800) , 50)
                if end_v == 2:
                    pg.draw.line(sc, (255, 0, 0), (750, 100),(750, 800) , 50)

                pg.display.update()
                print(end_v)
        for n in range(3):
            for m in range(3):
                if pole[n][m] == 0:
                    finish += 1
        if finish == 0 and win == False:
            stop = False


        pg.display.update()
    pg.time.delay(1)
