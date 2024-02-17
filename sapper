import random

import pygame as pg
import math


#'0' - нераскрытые поля
#'1' - раскрытые клетки без мин
#'2' - мины
#'3' - флажки
pg.font.init()
sc = pg.display.set_mode((960, 960))
sc.fill((0, 200, 0))
field= [[0 for f in range(16)] for l in range(16)]
f1 = pg.font.Font(None, 200)
f2 = pg.font.Font(None, 100)
end_text = f1.render('!БУМ!', True,(255, 0, 0))
end_pos = end_text.get_rect(center = (480, 480))
setup = True

flags_img = pg.image.load('flag.png')
flags_img = pg.transform.scale(flags_img, (60, 60))
color = (152, 251, 152)
for mine in range(random.randint(80, 100)):
    x_mine = random.randint(0, 15)
    y_mine = random.randint(0, 15)
    field[x_mine][y_mine] = 2
def print_field():
    for i in range(16):
        print(field[i])
def flag(x, y):
    f_x = math.ceil(x / (960 / 16))
    f_y = math.ceil(y / (960 / 16))
    print(field[f_x - 1][f_y - 1])
    if field[f_x - 1][f_y - 1] != 2:
        field[f_y - 1][f_x - 1] = 3
        pg.draw.rect(sc, color, ((f_x-1) * 60, (f_y-1) * 60, 60, 60))
        flag_rect = flags_img.get_rect(bottomright=(f_x*60+2, f_y * 60+2))
        sc.blit(flags_img, flag_rect)
   
    pg.display.update()
def first_cleek(x, y): #вскрытие первых нескольких клеток
    k_x = math.ceil(x / (960 / 16)) - 1
    k_y = math.ceil(y / (960 / 16)) - 1

    for s_x in range (k_x - 1, k_x +2):
        for s_y in range (k_y - 1, k_y +2):
            field[s_y][s_x] = 1
            pg.draw.rect(sc, color, (s_x * 60 , s_y * 60, 60, 60))
    r_x = random.randint(1, 2)
    r_y = random.randint(1, 2)

    for rx in range(k_x + r_x - 1, k_x + r_x + 1):
        for ry in range(k_y + r_y - 1, k_y + r_y + 1):
            field[ry][rx] = 1

    for x_cell in range(16):
        for y_cell in range(16):
            i_m = 0
            if field[x_cell][y_cell] == 1:
                # m_x = math.ceil(x_cell / (960 / 16)) - 1
                # m_y = math.ceil(y_cell / (960 / 16)) - 1
                m_x = y_cell
                m_y = x_cell
                for v_x in range(m_y - 1, m_y + 2):
                    for v_y in range(m_x - 1, m_x + 2):
                        if field[v_x][v_y] != 1:
                            if field[v_x][v_y] == 2 or field[v_x][v_y] == 3:
                                i_m += 1
                if i_m == 0:
                    for v_x in range(m_y - 1, m_y + 2):
                        for v_y in range(m_x - 1, m_x + 2):
                            field[v_x][v_y] = 1
                            pg.draw.rect(sc,color, (v_y*60, v_x*60, 60, 60))
                            pg.display.update()
            pg.draw.rect(sc, color, (k_x * 60 + ((r_x - 1) * 60),(k_y * 60 + ((r_y-1) * 60)), 120, 120))



   #for i in range(16):
    #    print(field[i])

def end(k_x, k_y): #функция окончания игры
    pg.draw.rect(sc, color, (k_y * 60 , k_x * 60, 60, 60))
    pg.draw.circle(sc, (0, 0, 0), (k_y * 60 + 30, k_x * 60 + 30), 20)

    pg.display.update()
    sc.blit(end_text, end_pos)


def sqare (x, y): #Открытие клеток
    k_x = math.ceil(x / (960 / 16)) - 1
    k_y = math.ceil(y / (960 / 16)) - 1
    print_field()


    if field[k_y][k_x] == 0:
        field[k_y][k_x] = 1
        pg.draw.rect(sc, color, (k_x*60, k_y*60, 60, 60))
        n = 0






    if field[k_y][k_x] == 2:
        end(k_y, k_x)
    pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            break

        for line in range(16):#рисование клеток
            pg.draw.line(sc,(0, 30, 0), (line * 60, 0), (line * 60, 960))
            pg.draw.line(sc,(0, 30, 0), (0, line * 60), (960, line * 60))
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if setup:
                first_cleek(x, y)
                setup = False

            else:
                sqare(x, y)
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            flag(x, y)
        for x_cell in range(16):
            for y_cell in range(16):
                i_m = 0

                if field[x_cell][y_cell] == 1:

                    #m_x = math.ceil(x_cell / (960 / 16)) - 1
                    #m_y = math.ceil(y_cell / (960 / 16)) - 1
                    m_x = y_cell
                    m_y = x_cell
                    for v_x in range(m_y - 1, m_y + 2):
                        for v_y in range(m_x - 1, m_x + 2):

                            if field[v_x][v_y] != 1:
                                if field[v_x][v_y] == 2 or field[v_x][v_y] == 3:

                                    i_m += 1
                    if i_m != 0:
                        num = pg.font.Font(None, 50)
                        txt = num.render(str(i_m), True, (0, 100, 0))
                        sc.blit(txt, txt.get_rect(center=((m_x+0.5)*60, (m_y+0.5) * 60)))
                        pg.display.update()




        pg.display.update()
