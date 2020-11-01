import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
rect(screen, (75, 170, 79), (0, 0, 600, 450))
rect(screen, (108, 93, 83), (0, 450, 600, 350))

# 1 столб желтые прямоугольники
rect(screen, (207, 174, 3), (0, 0, 40, 500))
# 2 столб
rect(screen, (207, 174, 3), (60, 0, 120, 760))
# 3 столб
rect(screen, (207, 174, 3), (390, 0, 40, 500))
# 4 столб
rect(screen, (207, 174, 3), (550, 0, 40, 620))

# ЁЖИК
# 1 ножка
ellipse(screen, (72, 55, 55), (350, 700, 22, 12))
ellipse(screen, (131, 125, 125), (350, 700, 22, 12), 1)
# 4 ножка
ellipse(screen, (72, 55, 55), (455, 700, 22, 12))
ellipse(screen, (131, 125, 125), (455, 700, 22, 12), 1)
# живот
ellipse(screen, (72, 55, 55), (355, 665, 120, 60))
ellipse(screen, (131, 125, 125), (355, 665, 120, 60), 1)
# 2 ножка
ellipse(screen, (72, 55, 55), (360, 710, 22, 12))
ellipse(screen, (131, 125, 125), (360, 710, 22, 12), 1)
# 3 ножкка
ellipse(screen, (72, 55, 55), (440, 718, 22, 12))
ellipse(screen, (131, 125, 125), (440, 718, 22, 12), 1)
# лицо
ellipse(screen, (72, 55, 55), (440, 670, 45, 35))
ellipse(screen, (131, 125, 125), (440, 670, 45, 35), 1)
# глаз 1
circle(screen, (0, 0, 0,), (458, 685), 4)
circle(screen, (131, 125, 125,), (458, 685), 4, 1)
# глаз 2
circle(screen, (0, 0, 0,), (468, 682), 4)
circle(screen, (131, 125, 125,), (468, 682), 4, 1)
# носик
circle(screen, (0, 0, 0,), (485, 690), 3)
circle(screen, (131, 125, 125,), (485, 690), 3, 1)
# иголки прямо
j = 1


def draw(x, y):




    polygon(screen, (36, 28, 28), [(360 + x, 680), (370 + x, 680), (365 + x, 642)])
    polygon(screen, (8, 6, 6), [(360 + x, 680), (370 + x, 680), (365 + x, 642)], 1)


while j <= 11:
    draw(-15 + (10 * j), 15)
    j += 1



# гриб
ellipse(screen, (225, 225, 225), (395, 622, 10, 40))
ellipse(screen, (154, 143, 143), (395, 622, 10, 40), 1)
ellipse(screen, (225, 0, 0), (380, 620, 40, 15))
ellipse(screen, (154, 143, 143), (380, 620, 40, 15), 1)
ellipse(screen, (225, 225, 225), (389, 622, 4, 2))
ellipse(screen, (154, 143, 143), (389, 621, 4, 2), 1)
ellipse(screen, (225, 225, 225), (400, 625, 6, 3))
ellipse(screen, (154, 143, 143), (400, 625, 6, 3), 1)
ellipse(screen, (225, 225, 225), (392, 628, 6, 4))
ellipse(screen, (154, 143, 143), (392, 628, 6, 4), 1)
ellipse(screen, (225, 225, 225), (410, 622, 3, 4))
ellipse(screen, (154, 143, 143), (410, 622, 3, 4), 1)
# фрукты
ellipse(screen, (220, 113, 55), (365, 650, 25, 30))
ellipse(screen, (154, 143, 143), (365, 650, 25, 30), 1)
ellipse(screen, (220, 113, 55), (375, 648, 28, 32))
ellipse(screen, (154, 143, 143), (375, 648, 28, 31), 1)
ellipse(screen, (254, 0, 0), (419, 650, 32, 32))
ellipse(screen, (154, 143, 143), (419, 650, 32, 33), 1)
p = 1


def draw1(x, y):

        polygon(screen, (36, 28, 28), [(360 + x + 5, 680 + y), (370 + x + 5, 680 + y), (365 + x + 5, 642 + y)])
        polygon(screen, (8, 6, 6), [(360 + x + 5, 680 + y), (370 + x + 5, 680 + y), (365 + x + 5, 642 + y)], 1)

        polygon(screen, (36, 28, 28), [(360 + x + 5, 680 + y*2), (370 + x + 5, 680 + y*2), (365 + x + 5, 642 + y*2)])
        polygon(screen, (8, 6, 6), [(360 + x + 5, 680 + y*2), (370 + x + 5, 680 + y*2), (365 + x + 5, 642 + y*2)], 1)



while p <= 11:
    draw1(-25 + (10 * p), 15, )
    p += 1






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
