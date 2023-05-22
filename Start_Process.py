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
        2层：黑色遮罩
    :param MainScreen: 主窗口
    """
    #     初始化阶段     #

    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_START_PROCESS):
        basic_func.new_layer(list(), list())

    # 初始化计时器
    start_process_clock = pygame.time.Clock()
    timer_for_mask = 0
    timer_for_press_space = 0

    #     加载阶段     #

    # 加载背景图片
    bgr = pygame.image.load("img/pictures/menu_bgr2.jpeg").convert()
    bgr = pygame.transform.scale(bgr, (1280, 1280))

    Global_Variable.MAIN_ATTACH[0].append(bgr)
    Global_Variable.MAIN_ATTACH_LOC[0].append((0, 0))

    # 加载空格进入提示
    press_space_font = pygame.font.Font("font/STXIHEI.TTF", 60)
    press_space = press_space_font.render("Press Space to Start", True, Global_Variable.WHITE)
    press_space.set_alpha(0)  # 初始不显示
    press_space_rect = press_space.get_rect()
    press_space_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2,
                               Global_Variable.WINDOW_SIZE[1] - press_space_rect.height)  # 底部居中

    Global_Variable.MAIN_ATTACH[1].append(press_space)
    Global_Variable.MAIN_ATTACH_LOC[1].append(press_space_rect)

    press_space_round = 0

    # 加载黑色遮罩
    mask = pygame.Surface(Global_Variable.WINDOW_SIZE, pygame.HWSURFACE | pygame.SRCALPHA)
    mask.fill(Global_Variable.BLACK)
    mask.set_alpha(255)

    Global_Variable.MAIN_ATTACH[2].append(mask)
    Global_Variable.MAIN_ATTACH_LOC[2].append((0, 0))

    #     生成与绘制阶段     #
    basic_func.gene_all_and_draw(MainScreen)

    end_of_start_process = False  # 是否结束该阶段的bool值
    while True:
        # 按键操作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not end_of_start_process:
                if event.key == pygame.K_SPACE:
                    end_of_start_process = True
                    break
        if end_of_start_process:
            break

        # 时间操作
        start_process_clock.tick()
        if mask.get_alpha() > 0:
            timer_for_mask += start_process_clock.get_time()
        timer_for_press_space += start_process_clock.get_time()

        # 画面操作
        if timer_for_mask >= 10 and mask.get_alpha() != 0:
            mask.set_alpha(max(mask.get_alpha() - 10, 0))
            timer_for_mask = 0
            basic_func.generate(2)

        if timer_for_press_space >= 20:
            press_space.set_alpha(basic_func.calculate_alpha(100, press_space_round % 100))
            timer_for_press_space = 0
            press_space_round += 1
            basic_func.generate(1)

        basic_func.draw(MainScreen)
    pygame.time.delay(100)
    # 初始化生成
    basic_func.init_global_generation()
    # 设置下一个页面
    Global_Variable.NEXT_PAGE = 1
