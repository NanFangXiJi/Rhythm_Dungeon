import sys
import pygame

import basic_func
import Global_Variable

import Menu
import Start_Process
import ToMap


# 初始化
pygame.init()
basic_func.read_obj_rule()  # 物体规则列表初始化
basic_func.init_obj_list()  # 物体列表初始化
del Global_Variable.obj_rule_list  # 物体初始化完毕后删除物体规则列表释放内存

# 开启主窗口
MainScreen = pygame.display.set_mode(Global_Variable.WINDOW_SIZE)
pygame.display.set_caption(Global_Variable.GAME_TITLE)
icon = pygame.image.load("img/pictures/icon.png")
pygame.display.set_icon(icon)

while True:
    if Global_Variable.NEXT_PAGE == 0:
        # 开始阶段
        Start_Process.start_process(MainScreen)
    elif Global_Variable.NEXT_PAGE == 1:
        # 菜单阶段
        Menu.menu(MainScreen)
    elif Global_Variable.NEXT_PAGE == 2:
        ToMap.ToMap(MainScreen)
