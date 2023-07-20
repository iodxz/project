from turtle import *
from random import *


shape('square')
screen = Screen()
screen.setup(1920, 1080, 0, 0)
start_x_wall = []
start_y_wall = []
end_x_wall = []
end_y_wall = []
healthy = []
sick = []
speed(11)
dead = []
shapesize(0.2)
peoples = []


def go():

    sick.append(peoples[0])
    sick[0].color('firebrick')
    i = 0
    while len(sick) != 0:

        for move in range(len(peoples)):
            x = randint(-10, 10)
            y = randint(-10, 10)

            #(bx - ax) * (py - ay) - (by - ay) * (px - ax)
            #s1 = ((end_x_wall[p_and_w] - start_x_wall[p_and_w]) * (peoples[move].ycor() - start_y_wall[p_and_w]) - (end_y_wall[p_and_w] - start_y_wall[p_and_w]) * (peoples[move].xcor() - start_x_wall[p_and_w]))
            #s2 = ((end_x_wall[p_and_w] - start_x_wall[p_and_w]) * (peoples[move].ycor() + y - start_y_wall[p_and_w]) - end_y_wall[p_and_w] - start_y_wall[p_and_w]) * (peoples[move].xcor() + x - start_x_wall[p_and_w]))
            #print(s1, s2)
            #for p_and_w in range(len(end_x_wall)):
                #if s1 > 0 and s2 > 0 or s1 < 0 and s2 < 0:
                    #peoples[move].goto(peoples[move].xcor() + x, peoples[move].ycor() + y)
            #for ill in range(sick):



        i += 1


def people(people_x, people_y):

    t = Turtle()
    t.color('dark green')
    t.penup()
    t.shape('circle')
    t.speed(0)
    t.shapesize(0.7)
    t.goto(people_x, people_y)
    t.speed(1)
    peoples.append(t)

    onkey(go, 'Return')
    screen.listen()


def build_wall():
    if len(start_x_wall) != len(end_x_wall):
        start_x_wall.pop(-1)
        start_y_wall.pop(-1)
    for w in range(len(start_x_wall)):
        penup()
        goto(start_x_wall[w], start_y_wall[w])
        pendown()
        goto(end_x_wall[w], end_y_wall[w])
    onscreenclick(people)


def wall(x_wall, y_wall):
    penup()
    goto(x_wall, y_wall)
    stamp()

    if len(start_x_wall) == len(end_x_wall):
        start_x_wall.append(x_wall)
        start_y_wall.append(y_wall)
    else:
        end_x_wall.append(x_wall)
        end_y_wall.append(y_wall)

    onkey(build_wall, 'Return')
    screen.listen()


onscreenclick(wall)
done()
