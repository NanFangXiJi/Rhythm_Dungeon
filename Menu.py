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
    #     初始化阶段     #

    # 初始化该阶段的所有图层
    for i in range(Global_Variable.LAYER_MENU):
        basic_func.new_layer(list(), list())

    #     加载阶段     #

    # 初始化计时器
    menu_clock = pygame.time.Clock()
    timer_for_mask = 0
    timer_for_press_space = 0

    # 加载背景图片
    bgr = pygame.image.load("img/pictures/menu_bgr2.jpeg").convert()
    bgr = pygame.transform.scale(bgr, (1280, 1280))

    Global_Variable.MAIN_ATTACH[0].append(bgr)
    Global_Variable.MAIN_ATTACH_LOC[0].append((0, 0))

    # 加载黑色遮罩
    mask = pygame.Surface(Global_Variable.WINDOW_SIZE, pygame.HWSURFACE | pygame.SRCALPHA)
    mask.fill(Global_Variable.BLACK)
    mask.set_alpha(255)

    # 加载标题文字
    title_font = pygame.font.Font("font/GIGI.TTF", 180)
    title = title_font.render(Global_Variable.GAME_TITLE, True, (255, 128, 128))
    title_rect = title.get_rect()
    title_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2, title_rect.height)

    Global_Variable.MAIN_ATTACH[1].append(title)
    Global_Variable.MAIN_ATTACH_LOC[1].append(title_rect)

    # 加载选择按钮
    option_font = pygame.font.Font("font/GIGI.TTF", 80)
    option1_text = option_font.render(">Enter game", True, (255, 255, 255))
    option1_rect = option1_text.get_rect()
    option1_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2, 600)

    option2_text = option_font.render(">Quit game", True, (255, 255, 255))
    option2_rect = option2_text.get_rect()
    option2_rect.center = (Global_Variable.WINDOW_SIZE[0] / 2, 800)

    Global_Variable.MAIN_ATTACH[2].append(option1_text)
    Global_Variable.MAIN_ATTACH_LOC[2].append(option1_rect)
    Global_Variable.MAIN_ATTACH[2].append(option2_text)
    Global_Variable.MAIN_ATTACH_LOC[2].append(option2_rect)

    option_round = 0

    #     生成与绘制阶段    #

    basic_func.gene_all_and_draw(MainScreen)

    # 播放背景音乐
    pygame.mixer.music.load("music/Sequel Blight.wav")
    pygame.mixer.music.play(-1)

    selected_option = 0  # 当前选中的选择支
    end_of_menu = False  # 是否结束该阶段的bool值
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and not end_of_menu:
                if event.key == pygame.K_SPACE:
                    if selected_option == 0:  # 进入游戏
                        end_of_menu = True
                        break
                    elif selected_option == 1:  # 退出游戏
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    if selected_option == 0:
                        option1_text.set_alpha(255)
                    elif selected_option == 1:
                        option2_text.set_alpha(255)
                    selected_option = (selected_option - 1) % 2
                elif event.key == pygame.K_DOWN:
                    if selected_option == 0:
                        option1_text.set_alpha(255)
                    elif selected_option == 1:
                        option2_text.set_alpha(255)
                    selected_option = (selected_option + 1) % 2

        # 让当前选项闪烁
        if selected_option == 0:
            # 时间操作
            menu_clock.tick()

            if mask.get_alpha() > 0:
                timer_for_mask += menu_clock.get_time()

            timer_for_press_space += menu_clock.get_time()

            if timer_for_mask >= 10 and mask.get_alpha() != 0:
                mask.set_alpha(max(mask.get_alpha() - 10, 0))
                timer_for_mask = 0
                basic_func.generate(2)

            if timer_for_press_space >= 20:
                option1_text.set_alpha(basic_func.calculate_alpha(100, option_round % 100))
                timer_for_press_space = 0
                option_round += 1
                basic_func.generate(1)
        elif selected_option == 1:
            # 时间操作
            menu_clock.tick()

            if mask.get_alpha() > 0:
                timer_for_mask += menu_clock.get_time()

            timer_for_press_space += menu_clock.get_time()

            if timer_for_mask >= 10 and mask.get_alpha() != 0:
                mask.set_alpha(max(mask.get_alpha() - 10, 0))
                timer_for_mask = 0
                basic_func.generate(2)

            if timer_for_press_space >= 20:
                option2_text.set_alpha(basic_func.calculate_alpha(100, option_round % 100))
                timer_for_press_space = 0
                option_round += 1
                basic_func.generate(1)

        # 生成与绘制阶段
        basic_func.gene_all_and_draw(MainScreen)

        if end_of_menu:
            break

    pygame.time.delay(100)
    # Global_Variable.music_channel[0].stop()
    pygame.mixer.music.stop()

    # 初始化生成
    basic_func.init_global_generation()
    # 设置下一个页面
    Global_Variable.NEXT_PAGE = 2
    Global_Variable.NEXT_MAP = 0
