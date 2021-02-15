import os
import pypresence
import pygame

#-*- coding:utf-8 -*-

#pyinstaller --icon=icon\\icon.ico -w --hidden-import=pygame cat.py

#---- reset ----#
pygame.init()
pygame.display.set_caption("PopCat")
rpc = Presence("DISCORD APP ID")
rpc.connect()

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
image5 = pygame.image.load(os.path.abspath("icon\\5.png"))
image6 = pygame.image.load(os.path.abspath("icon\\6.png"))
pygame.display.set_icon(image1)

#---- sound ----#
sound1 = pygame.mixer.Sound(os.path.abspath("sound\\1.wav"))
sound2 = pygame.mixer.Sound(os.path.abspath("sound\\2.wav"))

#---- font ----#
font = pygame.font.Font(os.path.abspath("font\\SCDream6.otf"), 30)
img1 = font.render('벌써 10000번 눌렀다.',True,(255, 255, 255))
img2 = font.render('이제 너 할꺼 하자구',True,(255, 255, 255))

#---- FPS ----#
FPS = 60
CLOCK = pygame.time.Clock()

#---- main loop ----#
crashed = False
condition = 1
ester = 0
nmb = 1000
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if ester >= nmb:
                    if condition == 1:
                        condition += 4
                    elif condition == 3:
                        condition += 3
                else:
                    condition += 1
                ester += 1
                if ester <= nmb*10:
                    sound2.play()
            elif event.key == pygame.K_z or event.key == pygame.K_LEFT:
                if condition == 1 or condition == 2:
                    condition += 2
                if condition == 5:
                    condition += 1
            elif event.key == pygame.K_x or event.key == pygame.K_RIGHT:
                if condition == 3 or condition == 4:
                    condition -= 2
                elif condition == 6:
                    condition -= 1
            if event.key == pygame.K_ESCAPE:
                crashed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if condition == 5:
                    condition -= 4
                elif condition == 6:
                    condition -= 3
                elif condition == 2 or condition == 4:
                    condition -= 1
                if ester <= nmb*10:
                    sound1.play()

    if ester >= nmb*10:
        screen.blit(img1, (50,350))
        screen.blit(img2, (70,400))
    else:
        if condition == 1:
            screen.blit(image1, (0, 0))
        elif condition == 2:
            screen.blit(image2, (0, 0))
        elif condition == 3:
            screen.blit(image3, (0, 0))
        elif condition == 4:
            screen.blit(image4, (0, 0))
        elif condition == 5:
            screen.blit(image5, (0, 0))
        elif condition == 6:
            screen.blit(image6, (0, 0))

    pygame.display.update()
    CLOCK.tick(FPS)
    rpc.update(state="PopCat", detalis="POP!", large_image="POP", start=ester" 번")

pygame.quit()