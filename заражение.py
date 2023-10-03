import random

import pygame as pg
import sys

sc = pg.display.set_mode((1000, 1000))
sc.fill((255, 255, 255))
pg.display.update()

start_wall = []
end_wall = []
dead = []
healthy = []
ill = []
peoples = []
GREEN = (0, 255, 0)
RED = (255, 0, 0)

counter = {} #FIXME


class section:
    def __init__(self, x1, y1):
        self.x = i.pos[0]
        self.y = i.pos[1]


def move(i):

    step = 0

    while True:
        print(counter)
        step += 1
        for close in pg.event.get():
            if close.type == pg.QUIT:
                sys.exit()
        sc.fill((255, 255, 255))
        pg.time.delay(100)
        for dot in range(len(start_wall)):
            pg.draw.rect(sc, (178, 34, 34), (start_wall[dot], (7, 7)))
            pg.draw.line(sc, (178, 34, 34), start_wall[dot], end_wall[dot], 5)
        for go in range(len(peoples)):
            ran_x = random.randint(-80, 80)
            ran_y = random.randint(-80, 80)
            x = peoples[go].x + ran_x
            y = peoples[go].y + ran_y

            if peoples[go] in healthy:
                pg.draw.circle(sc, GREEN, (x, y), 10)
            if peoples[go] in ill:
                pg.draw.circle(sc, RED, (x, y), 10)
            for ills in range(len(ill)):
                for dis in range(len(healthy) - 1, 0, -1):

                    r = ((healthy[dis].x - ill[ills].x) ** 2 + (healthy[dis].y - ill[ills].y) ** 2) ** 0.5
                    print(r)
                    if r < 100:
                        r = 0
                        probability_of_infection = random.randint(0, 1)
                        counter[go] = healthy[dis]
                        if probability_of_infection == 1:
                            counter[step] = healthy[dis]
                            ill.append(healthy[dis])
                            healthy.pop(dis)

        pg.display.update()


def draw_peoples():
    while True:
        for people in pg.event.get():
            if people.type == pg.QUIT:
                sys.exit()
            if people.type == pg.MOUSEBUTTONDOWN:
                if people.button == 1:

                    if len(ill) == 0:
                        human = pg.draw.circle(sc, (255, 0, 0), (people.pos[0], people.pos[1]), 10)
                        counter = {0: human}

                        pg.display.update()
                        ill.append(human)

                        peoples.append(human)
                    else:
                        human = pg.draw.circle(sc, (0, 255, 0), (people.pos[0], people.pos[1]), 10)

                        pg.display.update()
                        healthy.append(human)
                        peoples.append(human)
            if people.type == pg.KEYDOWN:
                if people.key == pg.K_SPACE:
                    move(i)


def wals():
    if len(start_wall) > len(end_wall):
        start_wall.pop(-1)
    for build_walls in range(len(end_wall)):
        pg.draw.line(sc, (178, 34, 34), start_wall[build_walls], end_wall[build_walls], 5)
        pg.display.update()
    draw_peoples()


def dots(i):
    if i.type == pg.MOUSEBUTTONDOWN:
        if i.button == 1:

            pg.draw.rect(sc, (178, 34, 34), (i.pos[0] - 2.5, i.pos[1] - 2.5, 7, 7))

            if len(start_wall) == len(end_wall):
                start_wall.append(i.pos)
            else:
                end_wall.append(i.pos)

            pg.display.update()
    if i.type == pg.KEYDOWN:
        if i.key == pg.K_SPACE:
            wals()


while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        pg.time.delay(1)
        dots(i)
