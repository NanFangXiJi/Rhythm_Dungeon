import sys
import pygame

import Global_Variable

import Start_Process

pygame.init()

# 开启主窗口
MainScreen = pygame.display.set_mode(Global_Variable.WINDOW_SIZE)
bgr = pygame.image.load("img/pictures/menu_bgr.png").convert()
def test01(MainScreen):
    MainScreen.blit(bgr, (0, 0))
    pygame.display.flip()
test01(MainScreen)
while True:
    pass