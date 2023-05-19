import pygame

import Global_Variable
import basic_func
def level(MainScreen: pygame.Surface):
    '''
    level阶段：
        0：背景
        1：标题文字
        2：关卡1
        3：关卡2
    :param Mainscreen: 主窗口
    '''

    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_MENU):
        basic_func.new_layer(list(), list())

    # ----生成----

    # 加载背景

    bgr = pygame.image.load("img/pictures/menu_bgr2.jpeg").convert()
    bgr = pygame.transform.scale(bgr, (1280, 1280))

    Global_Variable.MAIN_ATTACH[0].append(bgr)
    Global_Variable.MAIN_ATTACH_LOC[0].append((0, 0))

    # 加载标题

    title_font = pygame.font.Font("font/GIGI.TTF", 90)
    title = title_font.render("Rhythm Dungeon", True, (255, 128, 128))
    title_rect = title.get_rect()
    title_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2, title_rect.height)

    Global_Variable.MAIN_ATTACH[1].append(title)
    Global_Variable.MAIN_ATTACH_LOC[1].append(title_rect)

