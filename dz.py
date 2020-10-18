import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 625))

# golo i telo
circle(screen, (255, 213, 0), (400, 650), 160)
circle(screen, (218, 195, 195), (400, 400), 150)

# nos kista
polygon(screen, (67, 37, 37), [(385, 385), (415, 385), (400, 415)])
polygon(screen, (0, 0, 0), [(385, 385), (415, 385), (400, 415)], 1)

# rot
polygon(screen, (180, 50, 50), [(300, 425), (500, 425), (405, 481)])
polygon(screen, (0, 0, 0), [(300, 425), (500, 425), (405, 480)], 1)
# glaz
circle(screen, (39, 185, 255), (350, 350), 35)
circle(screen, (39, 185, 255), (450, 350), 35)
circle(screen, (0, 0, 0), (350, 351), 35, 1)
circle(screen, (0, 0, 0), (450, 351), 35, 1)
# glaznicha
circle(screen, (0, 0, 0), (340, 345), 15)
circle(screen, (0, 0, 0), (460, 345), 15)
# ruka 1 i 2
polygon(screen, (218, 195, 195), [(170, 175), (185, 165), (260, 515), (245, 520)])
polygon(screen, (218, 195, 195), [(630, 175), (615, 165), (540, 515), (555, 520)])
# plecho
polygon(screen, (255, 213, 0), [(270, 490), (300, 525), (285, 575), (230, 565), (225, 515)])
polygon(screen, (0, 0, 0), [(270, 490), (300, 525), (285, 575), (229, 565), (225, 515)], 1)
polygon(screen, (245, 213, 0), [(530, 490), (500, 525), (515, 575), (570, 565), (575, 515)])
polygon(screen, (0, 0, 0), [(530, 490), (500, 525), (520, 575), (571, 565), (575, 515)], 1)
# kista
ellipse(screen, (218, 195, 195), (160, 135, 55, 92))
ellipse(screen, (218, 195, 195), (585, 135, 55, 92))
# baner
rect(screen, (136, 170, 55), (150, 100, 500, 100))
rect(screen, (0, 0, 0), (150, 100, 500, 100), 2)
# bykavi
font_obj = pygame.font.Font('freesansbold.ttf', 45)
text_surface_obj = font_obj.render('PYTHON is AMAZING', True, (0, 0, 0), (136, 170, 55))
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (400, 150)
screen.blit(text_surface_obj, text_rect_obj)
# volosi
polygon(screen, (91, 30, 235), [(300, 284), (325, 271), (305, 255)])
polygon(screen, (0, 0, 0), [(300, 284), (325, 271), (305, 255)], 1)
polygon(screen, (91, 30, 235), [(500, 284), (475, 271), (495, 255)])
polygon(screen, (0, 0, 0), [(500, 284), (475, 271), (495, 255)], 1)
polygon(screen, (91, 30, 235), [(329, 269), (346, 260), (324, 247)])
polygon(screen, (0, 0, 0), [(329, 269), (346, 260), (324, 247)], 1)
polygon(screen, (91, 30, 235), [(471, 269), (456, 260), (476, 247)])
polygon(screen, (0, 0, 0), [(471, 269), (456, 260), (476, 247)], 1)
polygon(screen, (91, 30, 235), [(350, 259), (374, 254), (358, 235)])
polygon(screen, (0, 0, 0), [(350, 259), (374, 254), (358, 235)], 1)
polygon(screen, (91, 30, 235), [(450, 259), (426, 254), (442, 235)])
polygon(screen, (0, 0, 0), [(450, 259), (426, 254), (442, 235)], 1)
polygon(screen, (91, 30, 235), [(376, 253), (400, 251), (389, 232)])
polygon(screen, (0, 0, 0), [(376, 253), (400, 251), (389, 232)], 1)
polygon(screen, (91, 30, 235), [(424, 253), (400, 251), (411, 232)])
polygon(screen, (0, 0, 0), [(424, 253), (400, 251), (411, 232)], 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()