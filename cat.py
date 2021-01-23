import pygame
import os

#-*- coding:utf-8 -*-

#pyinstaller --onefile --icon=icon.ico -w --hidden-import=pygame cat.py

#---- reset ----#
pygame.init()
pygame.display.set_caption("PopCat")

#---- screen ----#
screen_size_1 = 512
screen_size_2 = 512
screen_size = screen_size_1, screen_size_2
screen = pygame.display.set_mode(screen_size)
pygame.mouse.set_visible(False)

#---- image ----#
on = os.getcwd()
image1 = pygame.image.load(os.path.abspath("icon\\1.png"))
image2 = pygame.image.load(os.path.abspath("icon\\2.png"))
image3 = pygame.image.load(os.path.abspath("icon\\3.png"))
image4 = pygame.image.load(os.path.abspath("icon\\4.png"))
pygame.display.set_icon(image1)

#---- FPS ----#
FPS = 60
CLOCK = pygame.time.Clock()

#---- main loop ----#
crashed = False
condition = 1
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                condition += 1
            elif event.key == pygame.K_z or event.key == pygame.K_LEFT:
                if condition == 1 or condition == 2:
                    condition += 2
            elif event.key == pygame.K_x or event.key == pygame.K_RIGHT:
                if condition == 3 or condition == 4:

                    condition -= 2
            if event.key == pygame.K_ESCAPE:
                crashed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                condition -= 1

    if condition == 1:
        screen.blit(image1, (0, 0))
    elif condition == 2:
        screen.blit(image2, (0, 0))
    elif condition == 3:
        screen.blit(image3, (0, 0))
    elif condition == 4:
        screen.blit(image4, (0, 0))

    pygame.display.update()
    CLOCK.tick(FPS)

pygame.quit()