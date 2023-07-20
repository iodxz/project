from turtle import *
hideturtle()
penup()
goto(-300, 300)
scr = Screen()
T = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.penup()
t2.penup()
t3.penup()

def t3_cor(x3, y3):
    t3.goto(x3, y3)
    T.penup()
    T.goto(t1.xcor(), t1.ycor())
    T.pendown()
    T.goto(t2.xcor(), t2.ycor())
    T.goto(t3.xcor(), t3.ycor())
    T.goto(t1.xcor(), t1.ycor())
    x1 = 'коор-ты 1 угла:', t1.xcor(), t1.ycor()
    x2 = 'коор-ты 2 угла:', t2.xcor(), t2.ycor()
    x3 = 'коор-ты 3 угла:', t3.xcor(), t3.ycor()
    write(x1,font=('Helvetica', 10, 'bold'))
    goto(-300, 280)
    write(x2, font=('Helvetica', 10, 'bold'))
    goto(-300, 260)
    write(x3, font=('Helvetica', 10, 'bold'))
    a = ((t2.ycor() - t1.ycor()) ** 2 + (t2.xcor() - t1.xcor()) ** 2)**0.5
    b = ((t3.ycor() - t2.ycor()) ** 2 + (t3.xcor() - t2.xcor()) ** 2)**0.5
    c = ((t3.ycor() - t1.ycor()) ** 2 + (t3.xcor() - t1.xcor()) ** 2)**0.5
    p = (a + b + c) / 2
    S ='S = ', (p * (p - a) * (p - b) * (p - c)) ** 0.5
    goto(-300, 240)
    write(S, font=('Helvetica', 12, 'bold'))
def t2_cor(x2,y2):
    t2.goto(x2, y2)
    onscreenclick(t3_cor)

def t1_cor(x1,y1):
    t1.goto(x1,y1)
    onscreenclick(t2_cor)

onscreenclick(t1_cor)




done()