import random
from turtle import*

w = Screen()
w.setup(1000, 700)
shape('circle')
shapesize(0.5)

try:
    angls = int(numinput('кол-во углов', prompt='ввод'))
except:
    angls = 3
try:
    points = int(numinput('кол-во точек', prompt='ввод'))
except:
    points = 10

a = 300

x, y = [], []
penup()
goto(a, a)
pendown()
inside = 0
outside = 0
speed(11)

for i in range(4):
    right(90)
    forward(2*a)
inside = []
tracer(0)
def WherePoint(xd, yd):
    if x[1]>x[0]:
        for o in range(0, len(x)-1):
            s = (x[o]-x[o+1])*(yd-y[o+1])-(y[o]-y[o+1])*(xd-x[o+1])
            #s:=(bx-ax)*(py-ay)-(by-ay)*(px-ax);
            if s < 0:
                return False
        return True
    else:
        for o in range(0, len(x)-1):
            s = (x[o]-x[o+1])*(yd-y[o+1])-(y[o]-y[o+1])*(xd-x[o+1])

            if s > 0:
                return False
        return True

def dots():
    color('black')
    shapesize(0.2)
    penup()
    int, out = 0, 0
    for i in range(points):
        xd = random.uniform(-a,a)
        yd = random.uniform(-a,a)
        goto(xd,yd)
        stamp()
        if WherePoint(xd,yd):
            int+=1

        else:
            out+=1


    hideturtle()
    goto(-450, 300)
    write(f'Внутри {int}', font=("Arial", 14, "normal"))
    goto(-450, 280)
    write(f'Снаружи {out}', font=("Arial", 14, "normal"))
    goto(-450, 260)
    write(f'S = {(int*(2*a)**2)/points} pnt', font=("Arial", 14, "normal"))
    return int, out



def move():
    x.append(x[0])
    y.append(y[0])
    penup()
    goto(x[0],y[0])
    for  i in range(angls):
        pendown()
        goto(x[i],y[i])
        stamp()

    goto(x[0], y[0])
    inside, outside = dots()

def go(X,Y):
    color('red')
    pensize(3)
    if len(x)>2:
        x.append(x[0])
        y.append(y[0])
        inn = WherePoint(X, Y)
        x.pop()
        y.pop()
        if inn:
            return
    penup()
    x.append(X)
    y.append(Y)
    goto(X,Y)
    stamp()
    if len(y) == angls:
        move()

onscreenclick(go)
done()