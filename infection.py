import pygame
import random
import math



# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
# Параметры окна
WIDTH, HEIGHT =750, 780 #1440, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Симуляция заражения")

# Персонажи и стены
infected = False
people = []
ill = []
walls = []
tik = []
count_ill = 0
count_death = 0
count_health = 0
size_edit_field = 30
death_threat = 0.0001
probability_of_recovery = 0.01
recovery_steps = 1500
probability_of_disease = 0.01
# Класс для персонажей
count = pygame.font.Font(None, 25)
edit = pygame.font.Font(None, 20)
# Радиус заражения (можете настроить это значение по своему усмотрению)
INFECTION_RADIUS = 70
switch = True
def ill_pers():
    people.append(Person(x, y, True))
class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, screen):
        # Рисуем прямоугольник кнопки
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        # Отображаем текст на кнопке
        font = pygame.font.SysFont('umeminchos3', 30)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=((self.x + self.width // 2), (self.y + self.height // 2)))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        # Проверяем, была ли нажата кнопка
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        else:
            return False



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
        if self.y + dy < 0 or self.y + dy > (HEIGHT-size_edit_field):
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
                if self.color == RED:
                    pygame.draw.circle(win, (200, 200, 210 ), (self.x, self.y), INFECTION_RADIUS, 1)
                    pygame.draw.circle(win, self.color, (self.x, self.y), 5)
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
# Определение кнопок
radius_down = Button(10, 750, 30, 30, "-", GRAY, BLACK)
radius_up = Button(110, 750, 30, 30, "+", GRAY, BLACK)

probability_of_disease_down = Button(160, 750, 30, 30, "-", GRAY, BLACK)
probability_of_disease_up = Button(260, 750, 30, 30, "+", GRAY, BLACK)

recovery_steps_down = Button(310, 750, 30, 30, "-", GRAY, BLACK)
recovery_steps_up = Button(410, 750, 30, 30, "+", GRAY, BLACK)

probability_of_recovery_down = Button(460, 750, 30, 30, "-", GRAY, BLACK)
probability_of_recovery_up = Button(560, 750, 30, 30, "+", GRAY, BLACK)

death_threat_down = Button(610, 750, 30, 30, "-", GRAY, BLACK)
death_threat_up = Button(710, 750, 30, 30, "+", GRAY, BLACK)
while running:
    # Проверяем события

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



        if event.type == pygame.MOUSEBUTTONDOWN:
            # Получаем позицию курсора
            pos = pygame.mouse.get_pos()
            if event.button == 1:
                n_edit_radius = 5
                n_edit_probability_of_disease = 0.01
                n_edit_recovery_steps = 100
                n_edit_probability_of_recovery = 0.01
                n_edit_death_threat = 0.0001
            if event.button == 3:
                n_edit_radius = 50
                n_edit_probability_of_disease = 0.1
                n_edit_recovery_steps = 1000
                n_edit_probability_of_recovery = 0.1
                n_edit_death_threat = 0.005
            # Проверяем, была ли нажата кнопка
            if radius_up.is_clicked(pos):
                INFECTION_RADIUS += n_edit_radius
            if radius_down.is_clicked(pos) and INFECTION_RADIUS - n_edit_radius >= 0:
                INFECTION_RADIUS -= n_edit_radius
            if probability_of_disease_up.is_clicked(pos) and probability_of_disease + n_edit_probability_of_disease <= 1:
                probability_of_disease += n_edit_probability_of_disease
            if probability_of_disease_down.is_clicked(pos) and probability_of_disease - n_edit_probability_of_disease >= 0:
                probability_of_disease -= n_edit_probability_of_disease
            if recovery_steps_down.is_clicked(pos) and recovery_steps - n_edit_recovery_steps >= 0:
                recovery_steps -= n_edit_recovery_steps
            if recovery_steps_up.is_clicked(pos):
                recovery_steps += n_edit_recovery_steps
            if probability_of_recovery_up.is_clicked(pos) and probability_of_recovery + n_edit_probability_of_recovery <= 1:
                probability_of_recovery += n_edit_probability_of_recovery
            if probability_of_recovery_down.is_clicked(pos) and probability_of_recovery - n_edit_probability_of_recovery >= 0:
                probability_of_recovery -= n_edit_probability_of_recovery
            if death_threat_up.is_clicked(pos) and death_threat + n_edit_death_threat <= 1:
                death_threat += n_edit_death_threat
            if death_threat_down.is_clicked(pos) and death_threat + n_edit_death_threat > 0:
                death_threat -= n_edit_death_threat
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
            if y <750:
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
    pygame.draw.line(win,BLACK,(0,750), (750, 750), 1)
    #Отрисовка кнопка
    radius_up.draw(win)
    radius_down.draw(win)
    probability_of_disease_down.draw(win)
    probability_of_disease_up.draw(win)
    recovery_steps_down.draw(win)
    recovery_steps_up.draw(win)
    probability_of_recovery_down.draw(win)
    probability_of_recovery_up.draw(win)
    death_threat_down.draw(win)
    death_threat_up.draw(win)
    count_persson = count.render('Total: '+str(len(people)), True, BLACK)
    ill = count.render('Sick: '+str(int(count_ill)), True, RED)
    healhy = count.render('Healthy: '+str(count_health), True, GREEN)
    death = count.render('Dead: '+str(count_death), True, False)
    win.blit(count_persson,(10,10))
    win.blit(ill, (10,25))
    win.blit(healhy, (10, 40))
    win.blit(death, (10, 55))

    radius_text = edit.render('radius', True, BLACK)
    radius_n = edit.render(str(INFECTION_RADIUS), True, BLACK)
    probability_of_disease_text = edit.render('Prob of D', True, BLACK)
    probability_of_disease_n = edit.render(str(round(probability_of_disease, 2)), True, BLACK)
    recovery_steps_text = edit.render('Steps of R', True, BLACK)
    recovery_steps_n = edit.render(str(recovery_steps), True, BLACK)
    probability_of_recovery_text = edit.render('Prob of R', True, BLACK)
    probability_of_recovery_n = edit.render(str(round(probability_of_recovery, 2)), True, BLACK)

    death_threat_text = edit.render('prob death', True, BLACK)
    death_threat_n = edit.render(str(round(death_threat, 4)), True, BLACK)
    win.blit(mode, (678, 8))
    # информация о редактировании параметров
    win.blit(radius_text,(50, 750))
    win.blit(radius_n,(65, 765))
    win.blit(probability_of_disease_text,(195, 750))
    win.blit(probability_of_disease_n, (210, 765))
    win.blit(recovery_steps_text, (342, 750))
    win.blit(recovery_steps_n, (360, 765))
    win.blit(probability_of_recovery_text, (495, 750))
    win.blit(probability_of_recovery_n, (515, 765))
    win.blit(death_threat_text, (640, 750))
    win.blit(death_threat_n, (665, 765))




    infect(people, walls)
    n_ill = 0
    n_dead = 0
    n_healthy = 0
        # Движение персонажей
    for person in people:
        if not person.is_dead:
            if person.infected_steps!=0:
                n_ill += 1
            if person.infected_steps==0:
                n_healthy += 1
        else:
            n_dead += 1

        count_death = n_dead
        count_ill = n_ill
        count_health = n_healthy
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
        if y <750:

            walls.append(pygame.Rect(x - 5, y - 5, 10, 10))
        # Рисуем стены
    for wall in walls:
        pygame.draw.rect(win, BLACK, wall)
    pygame.display.update()

    clock.tick(60)
pygame.quit()
