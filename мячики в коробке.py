from turtle import *


w = Screen()
w.setup(1920, 1080, 0, 0)
n = []
t1 = Turtle()
t1.shape('circle')
t1.penup()
t1.speed(0)
t1.shapesize(1.3)
t1.color('red')
while True:
    m1 = (numinput('enter the mass of the first ball', 'input', default=10000000))
    m2 = (numinput('enter the mass of the second ball', 'input', default=10000000))
    if int(m1) == m1 > 0 and int(m2) == m2 > 0:
        m1 = int(m1)
        m2 = int(m2)
        break

t2 = Turtle()
t2.shape('circle')
t2.penup()
t2.speed(0)
t2.shapesize(1.3)
t2.color('blue')

speed(0)
penup()
goto(950, 520)
pendown()
goto(950, -465)
goto(-950, -465)
goto(-950, 520)
goto(950, 520)


v1 = Turtle()
v1.penup()
v1.speed(0)
v1.penup()
v1.color('red')

v = []
v2 = Turtle()
v2.penup()
v2.speed(0)
v2.penup()
v2.color('blue')
shape('circle')
color('orange')


def end(x01, y01, x02, y02):
    penup()
    t1.goto(x01, y01)
    t2.goto(x02, y02)
    goto(x01, y01)
    for q in range(100):
        shapesize(q+10)
    done()


def go4(xv2, yv2):
    v2.goto(xv2, yv2)
    vx2 = (xv2 - t2.xcor()) / 50
    vy2 = (yv2 - t2.ycor()) / 50
    move(vx2, vy2, v[0], v[1])


def go3(xv1, yv1):
    v1.goto(xv1, yv1)
    vx1 = (xv1 - t1.xcor()) / 50
    vy1 = (yv1 - t1.ycor()) / 50
    v.append(vx1)
    v.append(vy1)

    onscreenclick(go4)


def go2(x2setup, y2setup):
    t2.goto(x2setup, y2setup)
    v2.goto(x2setup, y2setup)
    onscreenclick(go3)


def go1(x1setup, y1setup):
    t1.goto(x1setup, y1setup)
    v1.goto(x1setup, y1setup)
    onscreenclick(go2)


onscreenclick(go1)


def move(vx2, vy2, vx1, vy1):
    v1.hideturtle()
    v2.hideturtle()

    dx2 = vx2
    dy2 = vy2
    dx = vx1
    dy = vy1
    while True:
        x02, y02 = t2.position()
        x01, y01 = t1.position()
        r = ((x02 - x01) ** 2 + (y02 - y01) ** 2) ** 0.5
        f = (m1 * m2) / (r * r)

        fx1, fy1 = (x02-x01)/r, (y02-y01)/r
        fx1, fy1 = fx1 * f, fy1 * f
        fx2, fy2 = (x01-x02)/r, (y01-y02)/r
        fx2, fy2 = fx2 * f, fy2 * f

        ax1 = fx1 / m1
        ay1 = fy1 / m1
        ax2 = fx2 / m1
        ay2 = fy2 / m1

        v1x1 = dx + ax1 * 0.1
        v1y1 = dy + ay1 * 0.1
        v1x2 = dx2 + ax2 * 0.1
        v1y2 = dy2 + ay2 * 0.1

        if -950 < t1.xcor() < 950:
            if -465 < t1.ycor() < 520:
                print('1', x01+v1x1, y01 + v1y1)
                t1.goto(x01+v1x1, y01 + v1y1)

            else:
                t1.goto(x01 + v1x1, y01 - v1y1)

                dy = -dy
        else:
            t1.goto(x01 - v1x1, y01 + v1y1)

            dx = -dx

        if -950 < t2.xcor() < 950:
            if -465 < t2.ycor() < 520:
                print('2:', x02+v1x2, y02 + v1y2)
                t2.goto(x02+v1x2, y02 + v1y2)

            else:
                t2.goto(x02 + v1x2, y02 - v1y2)

                dy2 = -dy2
        else:
            t2.goto(x02 - v1x2, y02 + v1y2)

            dx2 = -dx2
        if r < 50:

            break
    end(x01, y01, x02, y02)


done()
