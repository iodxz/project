import pygame
import random
import math
import time
# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Параметры окна
WIDTH, HEIGHT =750, 750 #1440, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция заражения")

# Персонажи и стены
infected = False
people = []
walls = []
tik = []
count_ill = 0
count_death = 0
count_health = 0

death_threat = 0.0001
probability_of_recovery = 0.1
recovery_steps = 1500
probability_of_disease = 0.01
# Класс для персонажей
count = pygame.font.Font(None, 25)
# Радиус заражения (можете настроить это значение по своему усмотрению)
INFECTION_RADIUS = 70
switch = True
def ill_pers():
    people.append(Person(x, y, True))


class Person:
    def __init__(self, x, y, infected=False):
        self.x = x
        self.y = y
        self.color = RED if infected else GREEN
        self.vel = 10
        self.infected_steps = 0
        self.is_dead = False

    def move(self, dx, dy):
        # Проверяем границы экрана
        if self.check_collision(dx, dy):
            return
        if self.x + dx < 0 or self.x + dx > WIDTH:
            dx = -dx
        if self.y + dy < 0 or self.y + dy > HEIGHT:
            dy = -dy
        # Обновляем положение шара
        self.x += dx
        self.y += dy

    def check_collision(self, dx, dy):
        new_rect = pygame.Rect(self.x + dx, self.y + dy, 10, 10)
        for wall in walls:
            if new_rect.colliderect(wall):
                return True
        return False

    def draw(self):
        if self.is_dead:
            pygame.draw.circle(win, BLACK, (self.x, self.y), 5)
        else:
            pygame.draw.circle(win, self.color, (self.x, self.y), 5)

    def update(self):
        # Если персонаж заражен
        if self.color == RED:
            # Увеличиваем количество шагов с момента заражения
            self.infected_steps += 1

            # Проверяем вероятность выздоровления (10% на каждом шаге, но только после 100 ходов с момента заражения)
            if self.infected_steps >= recovery_steps and random.random() < probability_of_recovery:
                self.color = GREEN
                self.infected_steps = 0


            # Проверяем вероятность смерти (0,1% на каждом шаге)
            if random.random() < death_threat:
                self.is_dead = True


# Функция для вычисления расстояния между двумя точками
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)





# Функция для заражения персонажей, находящихся в пределах радиуса заражения
def infect(people, walls):
    for p1 in people:
        if p1.color == RED and not p1.is_dead:  # Проверяем только зараженных персонажей, которые не умерли
            for p2 in people:
                collision = False
                if p1 != p2 and p2.color == GREEN and not p2.is_dead:  #Проверяем только здоровых персонажей, которые не умерли
                    # Проверяем, находятся ли персонажи в пределах радиуса заражения
                    if distance((p1.x, p1.y), (p2.x, p2.y)) < INFECTION_RADIUS:
                        # Создаем отрезок между персонажами

                        # Проверяем пересечение этого отрезка со всеми стенами
                        for wall in walls:
                            wall_rect = pygame.Rect(wall)
                            if wall_rect.clipline(p1.x,p1.y,p2.x,p2.y):
                                collision = True
                                break
                        if round(random.random(), 2) <= probability_of_disease and collision == False:
                            p2.color = RED
                            p2.infected_steps = 0



# Основной цикл программы
clock = pygame.time.Clock()
running = True
main_i = 0
while running:
    # Проверяем события
    #print(count_death)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                if switch == False:
                    pygame.draw.rect(win, RED, (20, 20, 100, 75))

                    pygame.display.update()
                    switch = True
                elif switch == True:
                    switch = False
                print(switch)

        #if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_SPACE:
            #     press = True
            #     while press:
            #         if event.type == pygame.KEYUP:
            #             press = False
            #         time.sleep(0.1)

    # Расставляем персонажей по клику ПКМ
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = pygame.mouse.get_pos()
            tik.append(main_i)
            if switch == True:
                    ill_pers()

            else:
                people.append(Person(x, y))

    if running:  # Проверяем, закрыто ли окно
        win.fill(WHITE)
    if switch == False:
        pygame.draw.rect(win, GREEN, (720,0,750, 30))
    if switch == True:
        pygame.draw.rect(win, RED, (720,0,750, 30))
    mode = pygame.font.Font( None, 20)
    mode = mode.render('Mode:' , True, BLACK)


    count_persson = count.render('Total: '+str(len(people)), True, BLACK)
    ill = count.render('Sick: '+str(int(count_ill)-count_death), True, RED)

    healhy = count.render('Healthy: '+str(count_health), True, GREEN)
    death = count.render('Death: '+str(count_death), True, False)
    win.blit(count_persson,(10,10))
    win.blit(ill, (10,25))
    win.blit(healhy, (10, 40))
    win.blit(death, (10, 55))

    win.blit(mode, (678, 8))

    


    infect(people, walls)
        # Движение персонажей
    i_ill = 0
    i_death = 0
    i_health = 0
    for person in people:
        if person.color == RED:
            i_ill += 1
        if person.is_dead == True:
            i_death += 1
        if person.color == GREEN:
            i_health += 1
        count_health = i_health
        count_ill = i_ill
        count_death = i_death
        if person.is_dead != True:
            #print(person)
            # Присваиваем случайное (плавное) перемещение
            dx = random.uniform(-0.7, 0.7)
            dy = random.uniform(-0.7, 0.7)
            # Перемещаем персонажа, учитывая границы и столкновения со стенами
            person.move(dx * person.vel, dy * person.vel)
            person.update()
            person.draw()
            main_i += 1

        else:
            person.update()
            person.draw()

            main_i += 1
        # Ставим стены по нажатию ЛКМ
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        walls.append(pygame.Rect(x - 5, y - 5, 10, 10))
        # Рисуем стены
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)
    pygame.display.update()

    clock.tick(60)
pygame.quit()










