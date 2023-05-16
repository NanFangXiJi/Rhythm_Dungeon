import sys
import pygame

import Global_Variable
import basic_func

def menu(MainScreen: pygame.Surface):
    """
    menu阶段的层：
        0层：背景图片
        1层：标题文字
        2层：选择支
    :param MainScreen: 主窗口
    """
    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_MENU):
        basic_func.new_layer(list(), list())

    #     加载阶段     #

    # 加载背景图片
    bgr = pygame.image.load("img/pictures/menu_bgr.png").convert()

    Global_Variable.MAIN_ATTACH[0].append(bgr)
    Global_Variable.MAIN_ATTACH_LOC[0].append((0, 0))

    # 加载标题文字
    title_font = pygame.font.Font("font/GIGI.TTF", 90)
    title = title_font.render("Rhythm Dungeon", True, (255, 128, 128))
    title_rect = title.get_rect()
    title_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2, title_rect.height)

    Global_Variable.MAIN_ATTACH[1].append(title)
    Global_Variable.MAIN_ATTACH_LOC[1].append(title_rect)

    #     生成与绘制阶段    #

    basic_func.gene_all_and_draw(MainScreen)

    end_of_menu = False  # 是否结束该阶段的bool值
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
