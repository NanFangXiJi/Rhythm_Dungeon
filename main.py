import sys
import pygame

import Global_Variable
import Menu

import Start_Process
import basic_func

# 初始化
pygame.init()
basic_func.read_obj_rule()  # 物品规则列表初始化

# 开启主窗口
MainScreen = pygame.display.set_mode(Global_Variable.WINDOW_SIZE)
pygame.display.set_caption(Global_Variable.GAME_TITLE)
icon = pygame.image.load("img/pictures/icon.png")
pygame.display.set_icon(icon)

# 开始阶段
Start_Process.start_process(MainScreen)

while True:
    # 菜单阶段
    Menu.menu(MainScreen)
