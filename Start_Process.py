"""
控制进入标题画面以前的操作
"""
import sys
import pygame

import Global_Variable
import basic_func


def start_process(MainScreen: pygame.Surface):
    """
    start_process阶段的层：
        0层：背景图片
        1层：提示文字
    :param MainScreen: 主窗口
    """
    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_START_PROCESS):
        basic_func.new_layer(list(), list())

    #     加载阶段     #

    # 加载背景图片
    bgr = pygame.image.load("img/pictures/menu_bgr.png").convert()

    Global_Variable.MAIN_ATTACH[0].append(bgr)
    Global_Variable.MAIN_ATTACH_LOC[0].append((0, 0))

    # 加载空格进入提示
    press_space_font = pygame.font.Font("font/STXIHEI.TTF", 20)
    press_space = press_space_font.render("Press Space to Start", True, (255, 255, 255))
    press_space_rect = press_space.get_rect()
    press_space_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2,
                               Global_Variable.WINDOW_SIZE[1] - press_space_rect.height)  # 底部居中

    Global_Variable.MAIN_ATTACH[1].append(press_space)
    Global_Variable.MAIN_ATTACH_LOC[1].append(press_space_rect)

    #     生成阶段     #
    basic_func.generate()

    #     绘制阶段     #
    basic_func.draw(MainScreen)

    end_of_start_process = False  # 是否结束该阶段的bool值
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    end_of_start_process = True
                    break
        if end_of_start_process:
            break
