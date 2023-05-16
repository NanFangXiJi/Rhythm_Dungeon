import sys
import pygame

import Global_Variable

import Start_Process

pygame.init()

# 开启主窗口
MainScreen = pygame.display.set_mode(Global_Variable.WINDOW_SIZE)
pygame.display.set_caption(Global_Variable.GAME_TITLE)


Start_Process.start_process(MainScreen)

