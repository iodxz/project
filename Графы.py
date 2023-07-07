from turtle import*
speed(0)
w = Screen()
w.setup(1920, 1080, 0, 0)

while True:
    n = numinput('enter the number of cities', prompt='input')
    if int(n) == n > 0:
        n = int(n)
        break


shape('square')
shapesize(0.4)

x, y = [], []
in_tree = []


def build():
    hideturtle()
    in_tree.append(0)
    out_tree = [i for i in range(1, n)]
    goto(x[0], y[0])
    pendown()
    shapesize(0.0001)
    while len(out_tree) != 0:
        minimum = ((x[in_tree[0]] - x[out_tree[0]]) ** 2 + (y[in_tree[0]] - y[out_tree[0]]) ** 2) ** 0.5
        in_v = in_tree[0]
        out_v = out_tree[0]
        for i in in_tree:
            for j in out_tree:
                long = ((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2) ** 0.5
                if long < minimum:
                    minimum = long
                    in_v = i
                    out_v = j

        print('in_v =', in_v)
        print('out_tree=', out_tree)
        print('out_v=', out_v)
        print('in_tree', in_tree)
        penup()
        tracer(0)
        goto(x[in_v], y[in_v])
        pendown()
        goto(x[out_v], y[out_v])
        update()
        in_tree.append(out_v)
        out_tree.remove(out_v)


def go(x1, y1):
    penup()
    x.append(x1)
    y.append(y1)

    goto(x1, y1)

    stamp()
    if len(y) == n:

        build()


onscreenclick(go)

done()
