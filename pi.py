import random
from turtle import *
import matplotlib
import matplotlib.pyplot as plt
r = 200
a = 2*r
tracer(0)
w = Screen()
w.setup(1300, 700)
n = numinput('Ввод кол-ва точек', prompt = int)
n = int(n)
shape('circle')
pensize(1)
shapesize(0.1)
hideturtle()
speed(0)
penup()
goto(r, r)
pendown()
X = []
Y = []
p = []

for u in range(4):
    right(90)
    forward(a)
for i in range(n):
    p.append(3.14159265)
penup()
goto(0, 0)
right(90)
forward(r)
left(90)
pendown()
circle(r)
penup()
inside = 0
outside = 0
for i in range(1, n+1):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    goto(x,y)
    if xcor()**2 + ycor()**2 <= r**2:
        inside += 1
    else:
        outside += 1
    f = inside/(i)*4
    X.append(i)
    Y.append(f)
    stamp()
penup()
goto(-600, 310)
a = 'Оценка цисла Пи',(inside/n)*4
inside = 'в кругу:', inside
outside = 'не в кругу', outside
write(inside, font=("Arial", 14, "normal"))
goto(-600, 290)
write(outside, font=("Arial", 14, "normal"))
goto(-600, 270)
write(a, font=("Arial", 14, "normal"))
plt.plot(X, Y)
plt.plot(p)
plt.show()
done()
