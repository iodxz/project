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

# Параметры окна
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Симуляция заражения")

# Персонажи и стены
infected = False
people = []
walls = []
tik = []
death_threat = 0.0001
probability_of_recovery = 0.1
recovery_steps = 1000000
probability_of_disease = 0.5
# Класс для персонажей


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


# Радиус заражения (можете настроить это значение по своему усмотрению)
INFECTION_RADIUS = 70


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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Расставляем персонажей по клику ПКМ
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = pygame.mouse.get_pos()
            tik.append(main_i)
            if len(people) == 0:
                people.append(Person(x, y, True))
            else:
                people.append(Person(x, y))
    if running:  # Проверяем, закрыто ли окно
        win.fill(WHITE)
    infect(people, walls)

        # Движение персонажей
    for person in people:
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