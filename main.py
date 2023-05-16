import sys
import pygame

import Global_Variable
import Menu

import Start_Process

pygame.init()

# 开启主窗口
MainScreen = pygame.display.set_mode(Global_Variable.WINDOW_SIZE)
pygame.display.set_caption(Global_Variable.GAME_TITLE)

# 开始阶段
Start_Process.start_process(MainScreen)

while True:
    # 菜单阶段
    Menu.menu(MainScreen)
